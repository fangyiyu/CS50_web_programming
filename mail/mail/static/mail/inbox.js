document.addEventListener('DOMContentLoaded', function () {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#email-view').style.display = 'none';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

//checks if the string is email or not.
function validateEmail(email) {
  const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(String(email).toLowerCase());
}

function send_email() {

  //getting the values
  var recipients = document.querySelector('#compose-recipients').value;
  var subject = document.querySelector('#compose-subject').value;
  var body = document.querySelector('#compose-body').value;

  //check if the user has filled in the required parameters
  if (recipients != '') {

    //if the user entered multiple email addresses
    var recs = recipients.split(", ");

    //variable to track if all the emails entered are correct or not
    var validated = true;

    //checks if all the addresses (seperated by ", " are valid or not)
    for (mail in recs) {
      //if any of the email is not in the right format
      if (!validateEmail(recs[mail])) {
        validated = false;
      }
    }

    //if the addresses are all correct
    if (validated) {
      for (mail in recs) {
        //makes the POST request for the email address on which it is iterating
        fetch('/emails', {
          method: 'POST',
          body: JSON.stringify({
            recipients: recs[mail],
            subject: subject,
            body: body
          })
        })
          .then(response => response.json())
          .then(result => {
            // Print result
            console.log(result);

            var mes = document.querySelector('#message');
            //in case for any reason the email was not delivered
            if (result['error']) {

              //generates a message on that page.
              mes.innerHTML = `User with ${recs[mail]} does NOT exist`;
              mes.style.color = 'red';
            }

            //when the email is delivered
            else {
              mes.innerHTML = '';

              //load user's sent mailbox
              load_mailbox('sent');
            }
          });
      }
    }
    //if entered email addresses were not all correct
    else {
      var mes = document.querySelector("#message");
      mes.innerHTML = "Please enter valid email addresses seperated by \" ,\"";
      mes.style.color = "red";
    }

  }
  //if the parameters were not entered (the email address of the recipient is the only important thing here)
  else {
    var mes = document.querySelector("#message");
    mes.innerHTML = "Please enter one or more email addresses."
    mes.style.color = "red";
  }
}

//loads mailbox
function load_mailbox(mailbox) {

  var email_view = document.querySelector('#emails-view')
  document.querySelector('#email-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  // Show the mailbox and hide other views
  email_view.style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  email_view.innerHTML = '';
  email_view.innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  //GET request
  fetch(`/emails/${mailbox}`)
    .then(response => response.json())
    .then(emails => {

      if (emails.length == 0) {
        email_view.innerHTML = '<p style = "font-size: large; font-weight: bold;">Empty here</p>';
      }
      else {
        for (email in emails) {

          var mail = document.createElement("div");
          var sender = document.createElement('h5');
          var read = document.createElement('p');
          var sub = document.createElement('p');
          var time = document.createElement('p');
          var id = document.createElement('p');

          id.innerHTML = emails[email]['id'];
          id.style.display = 'none';
          sender.innerHTML = emails[email]['sender'];
          if (emails[email]['subject'] == '') {
            sub.innerHTML = 'No Subject';
            sub.style.color = '#AD7C62';
          }
          else {
            sub.innerHTML = emails[email]['subject'];
          }
          time.innerHTML = emails[email]['timestamp'];

          mail.style.borderStyle = 'solid';
          mail.style.borderColor = 'black';
          mail.style.borderWidth = '0.1rem';
          mail.style.marginBottom = '0.1rem';

          if (emails[email]['read'] == true) {
            read.innerHTML = 'Read';
            mail.style.backgroundColor = '#B5B3B0';
          }
          else {
            read.innerHTML = 'Unread';
            read.style.color = "red";
          }

          mail.classList.add('container');
          mail.classList.add('mail');

          sender.style.display = 'inline-block';
          sender.style.margin = '1rem';

          sub.style.display = 'inline-block';
          sub.style.margin = '1rem';

          read.style.display = 'inline-block';
          read.style.margin = '1rem';
          read.style.float = 'right';

          time.style.display = 'inline-block';
          time.style.margin = '1rem';
          time.style.float = 'right';
          time.style.color = 'black';

          email_view.append(mail);
          mail.append(sender);
          mail.append(sub);
          mail.append(time);
          mail.append(id);
          mail.append(read);

          //what happens when a user clicks on an email in the mailbox
          mail.addEventListener('click', () => load_email());
          sub.addEventListener('click', () => load_email());
          time.addEventListener('click', () => load_email());
          sender.addEventListener('click', () => load_email());
        }
      }
    }
    );
}

//shows the email you clicked on from mailbox
function load_email() {
  event.stopImmediatePropagation();
  //keeping only the email-view and hiding the rest
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  mail_view = document.querySelector('#email-view');
  mail_view.style.display = 'block';

  var tar = event.target;
  console.log(tar.children);

  //if the element clicked on is not div, we choose its parent (which is the div)
  if (!(tar.tagName == 'DIV')) {
    tar = tar.parentElement;
  }

  //we take the div's children elements and extract the id (we know that it is the fourth (third index) element as we checked using console.log)
  var c = tar.children;
  var id = c[3].innerHTML;

  //clearing old content
  mail_view.innerHTML = '';

  //we make a GET request to get everything we need about the email
  fetch(`/emails/${id}`)
    .then(response => response.json())
    .then(email => {

      //creating a div for each email in mailbox in which we will include sender, timestamp and subject 
      const div = document.createElement('div');

      //creating the needed elements for subject, sender, recipient etc.
      var sender = document.createElement('div');
      sender.innerHTML = "From:".bold() + email['sender'];
      var recipient = document.createElement('div');
      recipient.innerHTML= "To:".bold() + email['recipients'];
      var sub = document.createElement('div');
      sub.innerHTML= "Subject:".bold() + email['subject'];
      var time = document.createElement('div');
      time.innerHTML = "Timestamp:".bold() + email['timestamp'];
      var body = document.createElement('div');
      body.innerHTML = email['body'];

      //styling for timestamp
      time.style.color = 'black';
      time.classList.add('mb-3');

      //adding the elements to the div created
     
      div.append(sender);
      div.append(recipient);
      div.append(sub);
      div.append(time);

      //adding the div to the main div
      mail_view.append(div);

      //making the read attribute true in case it was false
      if (email['read'] == false) {
        //making the read attribute true
        fetch(`/emails/${id}`, {
          method: 'PUT',
          body: JSON.stringify({
            read: true
          })
        })
      }

      //Adding buttons from here on
      var archive = email['archived'];

      //archive toggle and reply button
      var btn = document.createElement('button');
      var reply = document.createElement('button');

      //setting buttons' inner text if the email is already archived
      if (archive) {
        btn.innerText = 'Unarchive';
      }
      else {
        btn.innerText = 'Archive';
      }
      reply.innerText = 'Reply';

      // adding bootstrap
      btn.classList.add('mr-2');
      btn.classList.add('btn-outline-primary');
      btn.classList.add('btn');
      reply.classList.add('btn-outline-primary');
      reply.classList.add('btn');

      //adding event listeners to both buttons

      //first the archive toggle
      btn.addEventListener('click', () => {
        //got this from the API documentation
        fetch(`/emails/${id}`, {
          method: 'PUT',
          body: JSON.stringify({
            archived: !archive
          })
        });
        //loading inbox after done toggling archive property
        load_mailbox('inbox');
      });

      //reply button function
      reply.addEventListener('click', () => {

        //opens the compose mail section and hides all the others
        compose_email();

        //setting default values as specified
        document.querySelector('#compose-recipients').value = email['sender'];
        document.querySelector('#compose-body').value = `On ${email['timestamp']}, ${email['sender']} wrote: ${email['body']}`;
        //checking for subject
        if (email['subject'].includes('Re:')) {
          document.querySelector('#compose-subject').value = email['subject'];
        }
        else {
          document.querySelector('#compose-subject').value = `Re: ${email['subject']}`;
        }
      });

      //adding the buttons to our HTML
      mail_view.append(btn);
      mail_view.append(reply);
      //styling for body
      body.classList.add('pt-3');
      body.classList.add('border-top');
      body.classList.add('my-3');
      // adding body to the main
      mail_view.append(body);
    });
}