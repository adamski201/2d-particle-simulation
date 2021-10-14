import matplotlib.pyplot as plt

def plot_xy(x, y):
    
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.xlabel("X")
    plt.ylabel("Y")
    