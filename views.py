from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User
import datetime
from binance.client import Client
import pandas as pd
from prophet import Prophet
import numpy as np
from django.views.decorators.csrf import ensure_csrf_cookie
from plotly.offline import plot
from plotly.graph_objs import *
from django.contrib import messages
from django.http import JsonResponse
import plotly.express as px
from django.views.generic import TemplateView

# Access your binance API keys from its website
client = Client('V6GT0mgwDWIqHzeCxlmJn0Q3BZPD9BCujEcobzr6Obz35leYAudRmGOrwsirof4U', 'uSaG10U4pgqKWD9WfoYbGCoXEAwn2XTkixIQlqL6h4Q6kWw3kFkRtCGXSFxhLZj1')

# Pull bitcoin data from Binance API
symbol = 'BTCUSDT'
BTC = client.get_historical_klines(symbol=symbol, interval = Client.KLINE_INTERVAL_1DAY  , start_str = '1 year ago UTC')
BTC = pd.DataFrame(BTC, columns=['Open time','Open','High','Low','Close','Volume','Close time','Quote asset volume','Number of trades','Taker buy base asset volume','Taker buy quote asset volume','ignored'])
BTC['Open time'] = pd.to_datetime(BTC['Open time'], unit='ms')
df_new=BTC[['Open time','Close']]

# Simple data preprocessing
df_new=df_new.rename(columns={'Open time':'ds','Close':'y'})
df_new['y'] = df_new['y'].astype(float)
df_old = df_new.copy()
df_new['y'] = np.log(df_new['y'])


def index(request):

    # Authenticated users can use the prediction tool
    if request.user.is_authenticated:
        return render(request, "app/index.html")

    # Everyone else is prompted to sign in
    else:
        return HttpResponseRedirect(reverse("login"))



# Prepare for graph using plotly.
# @login_required
# def graph(request):
#     x_data = np.array(df_old['ds'], dtype='datetime64[D]')
#     y_data = np.array(df_old['y'])
#     plot_div = plot([Scatter(x=x_data, y=y_data,
#                         mode='lines', name='test',
#                         opacity=0.8, marker_color='green')],
#                 output_type='div', include_plotlyjs=False,  show_link=False, link_text="")
                
#     return render(request, "app/index.html", {
#         'graph': plot_div
#         })


# tests
import plotly.offline as py
import plotly.graph_objs as go

class IndexView(TemplateView):
    template_name = "app/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plot'] = examplePlot()
        return context


def examplePlot():
    # Makes a simple plotly plot, and returns html to be included in template.
    x = np.linspace(0, 12.56, 41)
    y = np.sin(x)
    y2 = np.sin(1.2*x)

    data = [
        go.Scatter(
            name = 'Sin(x)',
            x=x,
            y=y,
        ),

        go.Scatter(
            name = 'Sin(1.2x)',
            x=x,
            y=y2,
        ),
    ]

    layout = go.Layout(
        xaxis=dict(
            title='x'
        ),

        yaxis=dict(
            title='Value',
            hoverformat = '.2f'
        ),
    )

    fig = go.Figure(data=data, layout=layout)
    plot_div = py.plot(fig, include_plotlyjs=False, output_type='div')

    return plot_div


# Predict using Facebook Prophet (ML model)
# @ensure_csrf_cookie
@login_required
def predict(request):
    if request.method == "POST":
        '''
        For rendering results on HTML GUI
        '''
        RequestDate = request.POST.get('market_dt')

        # Build model
        m=Prophet(interval_width=0.95, yearly_seasonality=True, weekly_seasonality=True,daily_seasonality=True, changepoint_prior_scale=2)
        m.add_seasonality(name='monthly', period=30.5, fourier_order=5, prior_scale=0.02)
        m.fit(df_new)
        future = m.make_future_dataframe(periods = 7,freq='D')

        # Predict
        forecast = m.predict(future)
        forecast = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
        forecast['yhat'] = np.exp(forecast['yhat'])
        forecast['yhat_lower'] = np.exp(forecast['yhat_lower'])
        forecast['yhat_upper'] = np.exp(forecast['yhat_upper'])

        result = forecast.loc[forecast['ds']==RequestDate]
        pred= result['yhat']
        opti_pred = result['yhat_upper']
        pers_pred = result['yhat_lower']

    return render(request, 'app/index.html', {
        "prediction_text": round(pred.values[0], 2),
        "optimistic_pred": round(opti_pred.values[0], 2),
        "perssimistic_pred": round(pers_pred.values[0], 2),
        "RequestDate": RequestDate})

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "app/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "app/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "app/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "app/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "app/register.html")

    