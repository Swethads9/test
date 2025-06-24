from flask import Flask, request, render_template_string
 
App = Flask(__name__)
 
# Inline HTML form with placeholders for result

html_form = """
<!DOCTYPE html>
<html>
<head>
<title>Addition App</title>
</head>
<body>
<h2>Add Two Numbers</h2>
<form method="get" action="/">
<label>Enter a: </label>
<input type="number" name="a" step="any" required><br><br>
<label>Enter b: </label>
<input type="number" name="b" step="any" required><br><br>
<input type="submit" value="Add">
</form>

    {% if result is not none %}
<h3>Result: {{ a }} + {{ b }} = {{ result }}</h3>

    {% endif %}
</body>
</html>

"""
 
@App.route('/', methods=['GET'])

def add():

    a = request.args.get('a')

    b = request.args.get('b')
 
    if a and b:

        try:

            a = float(a)

            b = float(b)

            result = a + b

            return render_template_string(html_form, a=a, b=b, result=result)

        except:

            return "Invalid input. Please enter numeric values."

    return render_template_string(html_form, result=None)
 
if __name__ == '__main__':

    App.run(host='0.0.0.0', port=5001)
 