from flask import Flask, jsonify, request
from config import db
import yaml
import os


class Message(db.Model):
    __tablename__='message'
    id= db.Column(db.Integer(), primary_key=True,autoincrement=True)
    fromUsers= db.relationship('users', lazy='select',
        backref=db.backref('message', lazy='joined'))
    toUsers= db.relationship('users', lazy='select',
        backref=db.backref('message', lazy='joined'))
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}