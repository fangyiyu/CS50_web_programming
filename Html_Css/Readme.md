1. Style an id using #id; style a class using .class; style an element using nothing.
2. Ways to deal with different screen sizes (responsive):
- adding 
``` html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
in head, 
to tell the mobile devices to use a viewport that is the same width as that of the device you're using rather than a much larger one.
- Through media queries.
- Through flexbox.
- Through grid.
- Including bootstrap in our html head by adding :
``` html
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
```
