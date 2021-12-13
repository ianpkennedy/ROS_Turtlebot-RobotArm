"""
This is the turtle kinematics package library file
"""
import math
from math import pi


def angx(w,h,peri,t):

    x = (w/2)*math.sin((2*pi*t)/peri)

    return x

def angxdot(w,h,peri,t):

    xdot = ((w*pi)/peri)*math.cos((2*pi*t)/peri)

    return xdot    

def angx2dot(w,h,peri,t):

    x2dot = -(2*w*pi*pi/(peri*peri))*math.sin((2*pi*t)/peri)

    return x2dot  


def angy(w,h,peri,t):

    y = (h/2)*math.sin((4*pi*t)/peri)

    return y 

def angydot(w,h,peri,t):

    ydot = ((2*h*pi)/peri)*math.cos((4*pi*t)/peri)

    return ydot

def angy2dot(w,h,peri,t):

    y2dot = -(8*h*pi*pi/(peri*peri))*math.sin((4*pi*t)/peri)

    return y2dot



def linmath(w,h,peri,t):
    """
    This function computes the appropriate linear velocity of the turtle
    Args:
        w (figure eight width in meters), h (figure eight height in meters), peri (shape period in seconds), t (time in seconds)
    
    Returns:
        lin_vel: linear velocity in m/s
    """
 
    xdot = ((w*pi)/peri)*math.cos((2*pi*t)/peri)
    ydot = ((2*h*pi)/peri)*math.cos((4*pi*t)/peri)
    lin_vel = math.sqrt(xdot*xdot+ydot*ydot)

    return lin_vel


def angmath(w,h,peri,t):
    """
    This function computes the appropriate angular velocity of the turtle
    Args:
        w (figure eight width in meters), h (figure eight height in meters), peri (shape period in seconds), t (time in seconds)
    
    Returns:
        ang_vel: angular velocity in rad/s
    """    
    
    xdot = ((w*pi)/peri)*math.cos((2*pi*t)/peri)
    ydot = ((2*h*pi)/peri)*math.cos((4*pi*t)/peri)
    x2dot = -(2*w*pi*pi/(peri*peri))*math.sin((2*pi*t)/peri)
    y2dot = -(8*h*pi*pi/(peri*peri))*math.sin((4*pi*t)/peri)
    ang_vel = ((y2dot*xdot)-(ydot*x2dot))/(xdot*xdot+ydot*ydot)

    return ang_vel

def anginit(w,h,peri,step):
    """
    This function computes the initial angle of the figure eight after the turtle is spawned
    Args: w (figure eight width in meters), h (figure eight height in meters), peri (shape period in seconds), step (time step in seconds)
  
    """

    xdot = ((w*pi)/peri)*math.cos((2*pi*step)/peri)
    ydot = ((2*h*pi)/peri)*math.cos((4*pi*step)/peri)
    x2dot = -(2*w*pi*pi/(peri*peri))*math.sin((2*pi*step)/peri)
    y2dot = -(8*h*pi*pi/(peri*peri))*math.sin((4*pi*step)/peri)


    ang_vel = ((y2dot*xdot)-(ydot*x2dot))/(xdot*xdot+ydot*ydot)

    ang = ang_vel*step

    x = (w/2)*math.sin((2*pi*step)/peri)
    y = (h/2)*math.sin((4*pi*step)/peri)

    theta = math.atan2(y,x)

    return theta



