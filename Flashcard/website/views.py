#Used for standard routing to webpages (designed in HTML)
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note, QuestionAnswer, User
from . import db
import json

views = Blueprint('views', __name__) #Best practice to Put var name and Args same as file name
global e
e = ' '

@views.route('/', methods=['GET', 'POST']) #Used to route the urls. We define what it does in the function underneath.
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        try:
            if len(note) < 1:
                flash('Link is too short!', category='error')
            else:
                new_note = Note(data=note, linkname = note, type = "plaintext", user_id=current_user.id)
                db.session.add(new_note)
                db.session.commit()
                flash('Set added!', category='success')
        except IndexError:
            flash('Invalid Num of Args', category='error')

        return redirect(url_for('views.setup', user=current_user, name = note, note_id = Note.query.all()[-1].id))
    
    else:
        return render_template('home.html', user=current_user)

@views.route('/setup/<name>/<note_id>', methods=['GET', 'POST'])
def setup(name, note_id):
    if request.form.get('question') == None or request.form.get('question') == "None" or request.form.get('question') == "" or request.form.get('question') == " ":
        pass
    else:
        new_qa = QuestionAnswer(question = request.form.get('question'), answer = request.form.get('answer'), questionanswer = note_id)
        db.session.add(new_qa)
        db.session.commit()
        flash('Question added!', category='success')
    
    try:
        if list(dict(request.form).values())[-1] == "finish":
            return redirect(url_for('views.home', user=current_user))
        else:
            return render_template('setup.html', user=current_user, nam = name)
    
    except IndexError:
        return render_template('setup.html', user=current_user, nam = name)



@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    for item in note.questions:
        print(item.question)
        print(item.answer)
    
    if note:
        if note.user_id == current_user.id:
            for item in note.questions:
                db.session.delete(item)
                db.session.commit()
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/study')
def study():
    return render_template("study.html", user=current_user)

@views.route('/<e>')
def hi(e):
    if e == "delete-note" or e == "study":
        pass
    else:
        idnum = 0
        condition = True
        for item in Note.query.all():
            if item.data == e:
                if item.user_id == current_user.id:
                    idnum = item.id
                else:
                    condition = False

            else:
                pass

        if condition:
            return render_template("info.html", user=current_user, id_num = idnum, totalqa = QuestionAnswer.query.all())
        else:
            return render_template("info.html", user=current_user)
    
        """
        print(User.query.all()[item.user_id-1])
        information = Note.query.all()
        #Accessing Set.
        for item in information:
            if item.data == e:
                idnum = item.id
            else:
                pass
        """    

