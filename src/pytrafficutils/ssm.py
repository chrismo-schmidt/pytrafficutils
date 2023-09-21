# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 12:00:26 2023

pytrafficutils.ssm

Surrogate safety measures for traffic analysis 

@author: Christoph M. Schmidt
"""

import numpy as np

def pet(t1, t2, ts):   
    '''Calculates the post encroachment time (PET) between the trajectories of
    two encroaching road users.
    
    The PET was introduced by Allen et al. (1978) and is a commonly used for
    surrogate safety assessment in traffic analysis and simulation. This 
    function measures the time between the first road user and the second user
    approximately occupying the same point in space. It does not perform 
    interpolation of the trajectories and does not consider the spatial extent
    of road users. 
    
    Assumes that t1 and t2 have at least one encroachment. If there is no 
    encroachmemt, the function returns the smallest distance in space.
    Finds the smallest encroachment time if there are multiple encroachments.

    Parameters
    ----------
    t1 : array
        Trajectory of the first road user.
    t2 : array
        Trajectory of the second road user.
    ts : float
        Sampling time.

    Returns
    -------
    float
        Post encroachment time.
    array
        Position of the encroachment in t1.
    TYPE
        Position of the encroachment in t2.

    References
    ----------
    Allen, B. L., Shin, B. T., & Cooper, P. J. (1978). Analysis of traffic 
    conflicts and collisions. Transportation Research Record, 667(1), 67–74.
    '''   
    dmin = 100000000.
    imint1 = 0
    imint2 = 0
    for i1 in range(t1.shape[1]):
        di = np.sqrt((t1[0,i1]-t2[0,:])**2+(t1[1,i1]-t2[1,:])**2)
        i2 = np.argmin(di)
        if di[i2] < dmin:
            dmin = di[i2]
            imint1 = i1
            imint2 = i2
    return abs((imint1-imint2)*ts), t1[:,imint1], t2[:,imint2]