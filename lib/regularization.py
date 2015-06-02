#!/usr/bin/env python
import inverse
import numpy as np

def regularization_matrix(param,p):
  slipreg = np.zeros((0,p['total']))
  slip_col = param['slip_collocation']
  flu_col = param['slip_collocation']
  slip_order = param['slip_regularization_order']
  flu_order = param['fluidity_regularization_order']
  slip_pen = param['slip_penalty']
  flu_pen = param['fluidity_penalty']
  slipreg = slip_pen*inverse.tikhonov_matrix(p['slip'],0,column_no=p['total'])
  flureg = flu_pen*inverse.tikhonov_matrix(p['fluidity'],0,column_no=p['total'])
  reg = np.vstack((slipreg,flureg))
  return reg

def priors(p):
  small = 1e-4
  big = 1e4
  Cp = small*np.eye(p['total'])
  Cp[p['fluidity'],p['fluidity']] = big
  Cp[p['slip'],p['slip']] = big
  Cp[p['secular_velocity'],p['secular_velocity']] = small
  Xp = np.zeros(p['total'])
  return Xp,Cp