from flask import Blurprint, render_template , request , redirect , url_for , flash

auth_bp = Blueprint('auth', __name__)

USER_CREDENTIALS = {
    'username' : 'admin'
    'password' : '1234'

}
    
