import matplotlib.pyplot as plt

def plot_xy(x, y):
    # create a scatter graph using matplotlib
    
    
    fig, ax = plt.subplots()
    ax.plot(x, y)
    
    # add axis labels and a title for clarity
    plt.xlabel("X / m")
    plt.ylabel("Y / m")
    plt.title("Trajectory of particle in 2 dimensions")
    