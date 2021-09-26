import json
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api

# https://www.datahound.org/api
@app.route('/api')
def dbs():
    return render_template("apps/database.html")
 
class ApoEspecies(Resource):
    def get(self, Org_name):
        data = ApoE.query.filter_by(Org_name=Org_name)
        return jsonify(data=[i.serialize for i in data.all()])
api.add_resource(ApoEspecies, '/api/species/<string:Org_name>')

class ApoERest(Resource):
    def get(self):
        data = ApoE.query.all()
        return jsonify(data=[i.serialize for i in data])
api.add_resource(ApoERest, '/api/all')

# Ideally this would happen in a seperate file, for example purposes see here.
class ApoE(db.Model):
    '''Example Model For Database ApoE from NCBI
    '''
    # fields
    pk = db.Column(db.Integer, primary_key=True)
    tax_id=db.Column(db.Integer)
    Org_name = db.Column(db.String(150), unique=False, nullable=True)
    GeneID= db.Column(db.String(150), unique=False, nullable=True)
    description= db.Column(db.String(150), unique=False, nullable=True)
    exon_count= db.Column(db.String(150), unique=False, nullable=True)

    def __repr__(self):
        return '<tax_id %r>' % self.tax_id
    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'pk'         : self.pk,
           'tax_id': self.tax_id,
           # This is an example how to deal with Many2Many relations
           'description'  : self.description,
           'Org_name':self.Org_name
       }

try:
    db.create_all()
except:
    print('already created')
