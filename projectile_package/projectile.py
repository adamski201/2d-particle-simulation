from numpy import sign

def update_state(t, p_x, p_y, v_x, v_y, a_x, a_y, dt=0.1):
    '''
    Update each parameter for the next time step.
    Args:
        t, p_x, p_y, v_x, v_y, a_x, a_y (float) : 
            time (s), position in X and Y axes (m), velocity in X and Y directions (m/s) and acceleration in X and Y directions (m/s2) values for this time step.
        dt (float) :
            time interval (s) for this small time step
    Returns:
        float, float, float, float, float : Updated values for t, p_x, p_y, v_x, v_y after this time step
    '''
    distance_moved_x = v_x*dt + (1/2)*a_x*(dt**2)
    distance_moved_y = v_y*dt + (1/2)*a_y*(dt**2)
    v_x += a_x*dt
    v_y += a_y*dt
    t += dt

    p_x += distance_moved_x
    p_y += distance_moved_y
    return t, p_x, p_y, v_x, v_y

def calculate_acceleration_y(v, k=0.0, mass=1.0, gravity=-9.81):
    '''
    Calculate the acceleration in the y-axis based on combined forces from gravity and 
    air resistance.
    Args:
        v (float) : 
            velocity (m/s) for this time step
        k (float) : 
            Combined air resistance coefficient, based on F=-kv^2. 
            Should be positive.
            Default = 0.0  i.e. no air resistance
        mass (float) : 
            Mass of the falling object. Needed if k > 0.
            Default = 1.0
        gravity (float) :
            Value for gravity to use when calculating gravitational force in m/s2.
            Default = -9.81
    Returns:
        float : accelaration calculated for this time step
    '''
    force_gravity = mass*gravity
    force_air = -sign(v)*k*v**2
    total_force = force_gravity + force_air
    a = total_force/mass
    
    return a

def calculate_acceleration_x(v, k=0.0, mass=1.0):
    '''
    Calculate the acceleration in the x-axis based on air resistance.
    Args:
        v (float) : 
            velocity (m/s) for this time step
        k (float) : 
            Combined air resistance coefficient, based on F=-kv^2. 
            Should be positive.
            Default = 0.0  i.e. no air resistance
        mass (float) : 
            Mass of the falling object. Needed if k > 0.
            Default = 1.0
    Returns:
        float : accelaration calculated for this time step
    '''
    force_air = -sign(v)*k*v**2
    a = force_air/mass
    
    return a

def flying_mass(initial_velocity_x=10.0, initial_velocity_y=10.0, k=0.0, mass=1.0):
    '''
    Model a flying projectile with a starting velocity of 10 m/s on both the X and Y axes.
    
    Args:
        initial_velocity_x (float) :
            Starting velocity on the x-axis.
            Default = 10.0 (m/s)
        initial_velocity_y (float) :
            Starting velocity on the y-axis.
            Default = 10.0 (m/s)
        k (float) :
            Combined air resistance coefficient, based on F=-kv^2. 
            Should be positive.
            Default = 0.0  i.e. no air resistance
        mass (float) :
            Mass of the object. Only needed if k is not 0.
            Default = 1.0  (kg)
    
    Returns:
        list, list, list, list, list : Five lists containing the time, positions along the X and Y axes, and velocities in X and Y directions.
    '''
    # Fixed input values
    gravity = -9.81 # m/s2

    # Initial values for our parameters
    p_x = 0.0 # x co-ordinate
    p_y = 0.0 # y co-ordinate
    v_x = initial_velocity_x
    v_y = initial_velocity_y
    t = 0.0

    # Create empty lists which we will update
    position_x = []
    position_y = []
    velocity_x = []
    velocity_y = []
    time = []

    # Keep looping while the object is still falling (y co-ordinate decreasing)
    while p_y > 0:
        # Evaluate the state of the system - start by calculating the total force on the object
        a_x = calculate_acceleration_x(v_x, k=k, mass=mass)
        a_y = calculate_acceleration_y(v_y, k=k, mass=mass, gravity=gravity)

        # Append values to list and then update
        position_x.append(position_x)
        position_y.append(position_y)
        velocity_x.append(v_x)
        velocity_y.append(v_y)
        time.append(t)

        # Update the state for time, and the position and velocity on the X and Y axes
        t, p_x, v_x = update_state(t, p_x, v_x, a_x, dt=0.1)
        t, p_y, v_y = update_state(t, p_y, v_y, a_y, dt=0.0)
    
    return time, position_x, position_y, velocity_x, velocity_y