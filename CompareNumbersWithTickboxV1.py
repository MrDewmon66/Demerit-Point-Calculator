# CompareNumbers
# With tick boxes v1

import os
from flask import Flask, render_template, request, flash

SUCCESS_MSG = 'success'
WARNING_MSG = 'warning'
KEY_SIZE = 24
HTML_TEMPLATE = 'compare_numbers_with_tickbox_1.html'

# Create Flask instance and set the session key
app = Flask(__name__)
app.secret_key = os.urandom(KEY_SIZE)

def compare_values(a,b):
    """ Compare values and retun a message string containing the result """

    if a > b:
        return f'{a} is larger than {b}.'
    elif a < b:
        return f'{a} is smaller than {b}.'
    else:
        return f'{a} is the same as {b}.' 
    

@app.route('/', methods = ['POST', 'GET'])
def home():
    """ Home page handler """

    print(f'DEBUG. Function received http method type: {request.method}')
    
    if request.method == 'POST':
        # Get the data that has been sent via http post
        first_num = request.form.get('form_first_number')
        second_num = request.form.get('form_second_number')
        tickbox1 = request.form.get('form_tickbox1')
        print(f'{tickbox1=}')
              
        if first_num != '' and second_num != '':
            # Data has been submitted
            if first_num.replace('.','').isdigit() and second_num.isdigit():
                # Numerical fields are digits so let's convert them to ints
                # Although we really should check to see if we should convert first_num to a float or an int 
                first_num = float(first_num)
                second_num = int(second_num)
                # Compare the values received and return the results to the browser
                msg = compare_values(first_num, second_num)
                flash(msg, SUCCESS_MSG)
                return render_template(HTML_TEMPLATE, title='CompareNumbers', form_first_number=first_num, form_second_number=second_num, form_tickbox1=tickbox1)
            else:
                # Not digits
                flash(f'Numbers only please.', WARNING_MSG)
        else:
            # Not all the data was received
            flash('Please enter two numbers please.', WARNING_MSG)

    return render_template(HTML_TEMPLATE, title='CompareNumbers')

if __name__ == '__main__':
    app.run()


