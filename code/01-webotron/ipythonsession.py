# coding: utf-8
import boto3
session = boto3.Session(profile_name = 'python_pgm_auto')
s3 = session.resource('s3')
