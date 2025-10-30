# CompareNumbers
# With tick boxes v1

import os
from flask import Flask, render_template, request, flash
from get_demerit_points import get_demerit_points

SUCCESS_MSG = 'success'
WARNING_MSG = 'warning'
KEY_SIZE = 24
HTML_TEMPLATE = 'compare_numbers_with_tickbox_1.html'

# Create Flask instance and set the session key
app = Flask(__name__)
app.secret_key = os.urandom(KEY_SIZE)

@app.route('/', methods = ['POST', 'GET'])
def home():
    """ Home page handler """

    print(f'DEBUG. Function received http method type: {request.method}')
    print(f"DEBUG form data: {request.form}")

    if request.method == 'POST':
        # Get the data that has been sent via http post
        driving_speed = request.form.get('form_driving_speed')
        speed_limit = request.form.get('form_speed_limit')
        holiday_period = request.form.get('form_holiday_period')
        print(f'{holiday_period=}')
              
        if driving_speed != '' and speed_limit != '':
            # Data has been submitted
            if driving_speed.replace('.','').isdigit() and speed_limit.isdigit():
                # Numerical fields are digits so let's convert them to ints
                # Although we really should check to see if we should convert first_num to a float or an int 
                driving_speed = float(driving_speed)
                speed_limit = int(speed_limit)
                # Compare the values received and return the results to the browser
                msg = get_demerit_points(driving_speed, speed_limit, holiday_period)
                flash(msg, SUCCESS_MSG)
                return render_template(HTML_TEMPLATE, title='CompareNumbers', form_driving_speed=driving_speed, form_speed_limit=speed_limit, form_holiday_period=holiday_period)
            else:
                # Not digits
                flash(f'Numbers only please.', WARNING_MSG)
        elif not driving_speed and speed_limit:
            # Only speed limit entered
            flash("Please enter a driving speed.", WARNING_MSG)
        elif driving_speed and not speed_limit:
            # Only driving speed entered
            flash("Please enter a speed limit.", WARNING_MSG)
        else:
            # No numbers entered
            flash('Please enter a driving speed and speed limit.', WARNING_MSG)

    return render_template(HTML_TEMPLATE, title='CompareNumbers')

if __name__ == '__main__':
    app.run()


