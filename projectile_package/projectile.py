def update_state(t, x, v, a, dt=0.1):
    '''
    Update each parameter for the next time step.
    Args:
        t, x, v, a (float) : 
            time (s), position (m) and velocity (m/s) and acceleration (m/s2) value for this time step.
        dt (float) :
            time interval (s) for this small time step
    Returns:
        float, float, float : Updated values for t, h, v after this time step
    '''
    distance_moved = v*dt + (1/2)*a*(dt**2)
    v += a*dt
    t += dt

    x += distance_moved
    
    return t, x, v

