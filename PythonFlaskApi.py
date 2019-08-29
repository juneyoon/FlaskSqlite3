from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Cooking, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///cookingmenu.db', connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route('/', methods=['GET','POST'])
def home():
    cooking = session.query(Cooking).all()
    return render_template('index.html', cooking=cooking)

@app.route('/menu/<int:cooking_id>/menu',methods=['GET','POST'])
def menuList(cooking_id):
    items = session.query(MenuItem).filter_by(cooking_id = cooking_id).all()
    return render_template('menu.html', items=items, cooking_id=cooking_id)

@app.route('/menu/<int:cooking_id>/new', methods=['GET','POST'])
def newMenuItem(cooking_id):
    if request.method == 'POST':
        newItem = MenuItem(name = request.form['name'], description = request.form['description'], cooking_id = cooking_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('menu.html', cooking_id = cooking_id))
    else:
      return render_template('newmenuitem.html', cooking_id = cooking_id)    

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0')
