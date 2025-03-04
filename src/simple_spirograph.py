import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

def draw_spirograph(R, r, d, num_points=1000, max_rotations=10,save_path=None):
    """
    Draw a spirograph using matplotlib
    
    Parameters:
    R (float): Radius of the fixed circle
    r (float): Radius of the moving circle
    d (float): Distance from the center of the moving circle
    num_points (int): Number of points to plot
    save_path (str): Path to save the figure, if None, figure is displayed
    
    Returns:
    The figure and axes objects
    """
    # Create a figure and axis
    fig = Figure(figsize=(10, 10))
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    
    # Parameter t
    t = np.linspace(0, 2 * np.pi * max_rotations, num_points)
    
    # Spirograph equations
    x = (R - r) * np.cos(t) + d * np.cos((R - r) * t / r)
    y = (R - r) * np.sin(t) - d * np.sin((R - r) * t / r)
    
    # Plot the spirograph
    ax.plot(x, y, '-', lw=1.5)
    ax.set_aspect('equal')
    ax.set_axis_off()
    ax.set_title(f'Spirograph (R={R}, r={r}, d={d})')
    
    # Add frame to the plot
    max_val = max(max(abs(x)), max(abs(y))) * 1.1
    ax.set_xlim(-max_val, max_val)
    ax.set_ylim(-max_val, max_val)
    
    # Save the figure if a path is provided
    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Figure saved to {save_path}")
    
    return fig, ax

if __name__ == "__main__":
    # Example parameters
    R = 23.0  # Radius of fixed circle
    r = 19.0  # Radius of moving circle
    d = 4.0  # Distance from center of moving circle
    
    # Draw and display the spirograph
    fig, ax = draw_spirograph(R, r, d, max_rotations=30,save_path="spirograph5.png")
    
    # Show the figure
    plt.figure(figsize=(10, 10))
    plt.imshow(np.array(fig.canvas.renderer.buffer_rgba()))
    plt.axis('off')
    plt.show()