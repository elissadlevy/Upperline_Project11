import os
from app import app
from flask import render_template, request, redirect
from datetime import datetime


from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'announcementsDB' 

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:uv4U6pAPuvwVmfSA@cluster0-qezhz.mongodb.net/announcementsDB?retryWrites=true&w=majority' 

mongo = PyMongo(app)


# INDEX

@app.route('/')
@app.route('/index')

def index():
    collection = mongo.db.announcementsList
    # find data
    allAnnouncements = collection.find({}).sort("submitTime", -1)
    
    return render_template('index.html', allAnnouncements = allAnnouncements)

#New Announcement Route
@app.route('/newannouncement')

def newannouncement():
    return render_template('newannouncement.html')

#Confirmation Route
@app.route('/confirmation', methods=['GET', 'POST'])

def confirmation():
    if request.method == "GET":
        return redirect('/')
    else:
        submitterName = request.form['submitterName']
        clubOrGroup = request.form['clubOrGroup']
        startDate = request.form['startDate']
        endDate = request.form['endDate']
        myAnnouncement = request.form['myAnnouncement']
        
        collection = mongo.db.announcementsList
        collection.insert({"submitTime":datetime.now(), "submitter": submitterName, "clubOrGroup": clubOrGroup, "startDate": startDate, "endDate": endDate, "myAnnouncement": myAnnouncement })
        return render_template('confirmation.html')
        
#Announcements for a specific clubOrGroup
@app.route('/clubOrGroup/<clubOrGroup>')

#THIS PART DOESN'T WORK YET - NEED TO FIGURE OUT WHY!!!!
def clubOrGroup(clubOrGroup):
    collection = mongo.db.announcementsList
    allAnnouncements = collection.find({"clubOrGroup":clubOrGroup}).sort("submitTime", -1)
    
    return render_template('club.html', allAnnouncements = allAnnouncements)