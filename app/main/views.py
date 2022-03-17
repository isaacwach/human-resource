from flask import flash, render_template,request,redirect,url_for,abort
from flask_login import login_required
from .. import db
from app.main.forms import CreateProfile
from . import main
from app.models import Profile, User

# Views
@main.route('/')
def index():

    return render_template('index.html')


@main.route('/home')
def home():

    return render_template('home.html')

@main.route('/dashboard', methods=['GET','POST'])
def dashboard():
    form= CreateProfile()
    if form.validate_on_submit():
        profile = Profile(fullname=form.fullname.data, position=form.position.data, job_id=form.job_id.data,department=form.department.data, awards = form.awards.data, experience=form.experience.data)
        db.session.add(profile)
        db.session.commit()
        return redirect(url_for('.dashboard'))

    flash('Profile Successfully Updated')
    profiles = Profile.query.all()
    
    

    return render_template('dashboard.html', form=form, profiles=profiles)

# @main.route('/dashboard')
# def dashboard():
#     '''supposed to query info '''
#     pass


# @main.route('/logout')
# def logout():
#     return render_template('index.html')



# @main.route('/user/<uname>')
# def dashboard(uname):
#     user = User.query.filter_by(username=uname).first()

#     if user is None:
#         abort(404)

#     return render_template('dashboard.html', user=user)


# @main.route('/user/<uname>/update',methods = ['GET','POST'])
# @login_required
# def update_dashboard(uname):
#     user = User.query.filter_by(username = uname).first()
#     if user is None:
#         abort(404)

#     form = UpdateExperience()

#     if form.validate_on_submit():
#         user.experience = form.experience.data
#         user.awards = form.awards.data


#         db.session.add(user)
#         db.session.commit()

#         return redirect(url_for('.dashboard',uname=user.username))

#     return render_template('updatedasboard.html',form =form)

