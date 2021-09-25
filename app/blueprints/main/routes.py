from app.blueprints.main.models import MarvelCharacter as MC
from app.blueprints.auth.models import User
from app import db
from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user
from .import bp as app



# @app.route('/', methods=['GET','POST'])
# def home():
#     if request.method == 'POST':
#         p = Post(
#                 body=request.form.get('body'),
#                 user_id=current_user.user_id
#             )
#         db.session.add(p)
#         db.session.commit()
#         flash('Post created successfully', 'success')

#         return redirect(url_for('main.home'))

#     context = {
#         'Characters': MC.query.order_by(MC.date_created.desc()).all()
#     }
#     return render_template('home.html',**context)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        char = MC(
            name=request.form.get('name'),
            description=request.form.get('desc'),
            comics_appeared_in=request.form.get('comics'),
            super_power=request.form.get('powers'),
            owner=current_user.id
        )
        db.session.add(char)
        db.session.commit()
        flash('Character created successfully','success')

        return redirect(url_for('main.home'))
    
    

    return render_template('Characters.html')

@app.route('/profile', methods=['GET','POST','DEL'])
def profile():
    context = {
                    'characters': MC.query.order_by(MC.date_created.desc()).all()
                }
    if request.method == 'DEL':
        flash('Character Deleted')

        return redirect(url_for('main.profile'))

        
    return render_template('profile.html', **context)