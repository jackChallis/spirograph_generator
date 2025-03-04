import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def create_colorful_spirograph(save_path=None):
    """
    Create a colorful spirograph with multiple patterns
    
    Parameters:
    save_path (str): Path to save the figure, if None, figure is displayed
    """
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 12), facecolor='black')
    ax.set_facecolor('black')
    
    # Parameter space
    t = np.linspace(0, 2 * np.pi * 30, 10000)
    
    # List of parameter combinations
    patterns = [
        # (R, r, d, color)
        (8.0, 1.0, 4.0, 'viridis'),
        (7.0, 3.0, 3.5, 'plasma'),
        (9.0, 2.0, 3.0, 'inferno'),
        (6.0, 2.3, 2.5, 'magma'),
        (7.5, 1.5, 3.8, 'cividis')
    ]
    
    # Plot each pattern
    for i, (R, r, d, colormap) in enumerate(patterns):
        # Calculate spirograph curves
        x = (R - r) * np.cos(t) + d * np.cos((R - r) * t / r)
        y = (R - r) * np.sin(t) - d * np.sin((R - r) * t / r)
        
        # Create colors that change with parameter t
        colors = cm.get_cmap(colormap)(np.linspace(0, 1, len(t)))
        
        # Plot segments with changing colors
        for j in range(len(t)-1):
            ax.plot(x[j:j+2], y[j:j+2], '-', color=colors[j], linewidth=1.0, alpha=0.8)
    
    # Set aspect ratio and remove axes
    ax.set_aspect('equal')
    ax.set_axis_off()
    
    # Set plot limits
    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    
    # Set title
    ax.set_title("Colorful Spirograph Collection", color='white', fontsize=16)
    
    # Save the figure if a path is provided
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='black')
        print(f"Figure saved to {save_path}")
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    create_colorful_spirograph(save_path="colorful_spirograph.png") 