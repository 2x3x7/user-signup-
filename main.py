from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/signup", methods=['POST'])
def welcome():
    user_name = request.form['user_name']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    user_name.strip()
    password.strip()
    verify_password.strip()
    email.strip()

    empty_form=''

    if user_name == empty_form:
        return redirect("/?username_error=Please provide a username.")
    if " " in user_name:
        return redirect("/?name_space_error=Spaces are not valid for username.")
    if len(user_name) < 3 or len(user_name) > 20:
        return redirect("/?name_length_error=Username must be between 3 and 20 characters long.")

    if password == empty_form:
        return redirect("/?password_error=Please provide a password.")
    if verify_password == empty_form:
        return redirect("/?verify_error=Please verify your password.")
    if password != verify_password:
        return redirect("/?match_error=Passwords do not match.")
    if len(password) < 3 or len(password) > 20:
        return redirect("/?pass_length_error=Password must be between 3 and 20 characters long.")

    if email != empty_form:
        if " " in email:
            return redirect("/?email_space_error=Spaces are not valid for email.")
        if len(email) < 3 or len(email) > 20:
            return redirect("/?email_length_error=Email must be between 3 and 20 characters long.")
        if "@" not in email or "." not in email:
            return redirect("/?sym_error= Symbols missing from email.")

    
    return render_template('welcome_user.html', name=user_name)
   


@app.route("/")
def index():
    error = {
    'username_error': "",
    'name_length_error': "", 
    'name_space_error': "",
    'password_error': "", 
    'verify_error': "", 
    'match_error': "", 
    'pass_length_error': "",
    'email_length_error': "",
    'email__space_error': "",
    'sym_error': "",}

    username_error = request.args.get("username_error")
    if username_error:
        error_esc = cgi.escape(username_error, quote=True)
        error['username_error'] =  error_esc 

    name_length_error = request.args.get("name_length_error")
    if name_length_error:
        error_esc = cgi.escape(name_length_error, quote=True)
        error['name_length_error'] =  error_esc 

    name_space_error = request.args.get("name_space_error")
    if name_space_error:
        error_esc = cgi.escape(name_space_error, quote=True)
        error['name_space_error'] =  error_esc 

    password_error = request.args.get("password_error")
    if password_error:
        error_esc = cgi.escape(password_error, quote=True)
        error['password_error'] =  error_esc 

    verify_error = request.args.get("verify_error")
    if verify_error:
        error_esc = cgi.escape(verify_error, quote=True)
        error['verify_error'] =  error_esc 

    match_error = request.args.get("match_error")
    if match_error:
        error_esc = cgi.escape(match_error, quote=True)
        error['match_error'] =  error_esc
    
    pass_length_error = request.args.get("pass_length_error")
    if pass_length_error:
        error_esc = cgi.escape(pass_length_error, quote=True)
        error['pass_length_error'] =  error_esc 

    email_length_error = request.args.get("email_length_error")
    if email_length_error:
        error_esc = cgi.escape(email_length_error, quote=True)
        error['email_length_error'] =  error_esc 

    email_space_error = request.args.get("email_space_error")
    if email_space_error:
        error_esc = cgi.escape(email_space_error, quote=True)
        error['email_space_error'] =  error_esc 

    sym_error = request.args.get("sym_error")
    if sym_error:
        error_esc = cgi.escape(sym_error, quote=True)
        error['sym_error'] =  error_esc 

    return render_template('user_signup.html', error=error)


app.run()