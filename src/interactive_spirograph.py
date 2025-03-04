import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, TextBox
from matplotlib.figure import Figure

def create_interactive_spirograph():
    """
    Create an interactive spirograph where you can adjust parameters with sliders
    or by typing in specific values
    """
    # Initial parameters
    R_init = 8.0  # Radius of fixed circle
    r_init = 1.0  # Radius of moving circle
    d_init = 4.0  # Distance from center of moving circle
    
    # Create the figure and axis with higher DPI for sharper rendering
    fig, ax = plt.subplots(figsize=(10, 8), dpi=120)
    plt.subplots_adjust(bottom=0.35)  # Make even more room for controls
    
    # Increase the number of points for smoother curves
    num_points = 3000
    t = np.linspace(0, 2 * np.pi * 10, num_points)
    
    # Initial spirograph calculation
    x = (R_init - r_init) * np.cos(t) + d_init * np.cos((R_init - r_init) * t / r_init)
    y = (R_init - r_init) * np.sin(t) - d_init * np.sin((R_init - r_init) * t / r_init)
    
    # Create the line plot with higher quality
    line, = ax.plot(x, y, '-', lw=1.0)
    ax.set_aspect('equal')
    ax.set_axis_off()
    ax.set_title(f'Spirograph (R={R_init:.2f}, r={r_init:.2f}, d={d_init:.2f})')
    
    # Set axis limits with some padding
    max_val = max(max(abs(x)), max(abs(y))) * 1.1
    ax.set_xlim(-max_val, max_val)
    ax.set_ylim(-max_val, max_val)
    
    # Create sliders for each parameter
    ax_R_slider = plt.axes([0.25, 0.20, 0.65, 0.03])
    ax_r_slider = plt.axes([0.25, 0.15, 0.65, 0.03])
    ax_d_slider = plt.axes([0.25, 0.10, 0.65, 0.03])
    
    slider_R = Slider(ax_R_slider, 'R', 1.0, 15.0, valinit=R_init)
    slider_r = Slider(ax_r_slider, 'r', 0.1, 5.0, valinit=r_init)
    slider_d = Slider(ax_d_slider, 'd', 0.1, 10.0, valinit=d_init)
    
    # Create text boxes for manual input
    ax_R_text = plt.axes([0.1, 0.20, 0.1, 0.03])
    ax_r_text = plt.axes([0.1, 0.15, 0.1, 0.03])
    ax_d_text = plt.axes([0.1, 0.10, 0.1, 0.03])
    
    text_R = TextBox(ax_R_text, 'R = ', initial=str(R_init))
    text_r = TextBox(ax_r_text, 'r = ', initial=str(r_init))
    text_d = TextBox(ax_d_text, 'd = ', initial=str(d_init))
    
    def update_from_sliders(val=None):
        """Update the spirograph based on slider values"""
        # Get current slider values
        R = slider_R.val
        r = slider_r.val
        d = slider_d.val
        
        # Update text boxes to match sliders (without triggering their callbacks)
        text_R.set_val(f"{R:.2f}")
        text_r.set_val(f"{r:.2f}")
        text_d.set_val(f"{d:.2f}")
        
        # Update the spirograph
        update_spirograph(R, r, d)
    
    def update_from_text_R(text):
        """Handle R text box input"""
        try:
            value = float(text)
            # Constrain to slider limits
            value = max(1.0, min(15.0, value))
            # Update slider (which will trigger update_from_sliders)
            slider_R.set_val(value)
        except ValueError:
            # If invalid input, revert to current slider value
            text_R.set_val(f"{slider_R.val:.2f}")
    
    def update_from_text_r(text):
        """Handle r text box input"""
        try:
            value = float(text)
            # Constrain to slider limits
            value = max(0.1, min(5.0, value))
            # Update slider (which will trigger update_from_sliders)
            slider_r.set_val(value)
        except ValueError:
            # If invalid input, revert to current slider value
            text_r.set_val(f"{slider_r.val:.2f}")
    
    def update_from_text_d(text):
        """Handle d text box input"""
        try:
            value = float(text)
            # Constrain to slider limits
            value = max(0.1, min(10.0, value))
            # Update slider (which will trigger update_from_sliders)
            slider_d.set_val(value)
        except ValueError:
            # If invalid input, revert to current slider value
            text_d.set_val(f"{slider_d.val:.2f}")
    
    def update_spirograph(R, r, d):
        """Update the spirograph with given parameters"""
        # Handle edge case to prevent division by zero
        if abs(r) < 0.01:
            r = 0.01
            
        # Calculate LCM for determining pattern period
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        def lcm(a, b):
            return abs(a * b) // gcd(a, b) if a and b else 0
        
        # Calculate appropriate number of cycles based on the ratio of R to r
        cycles = 10
        if r != 0:
            ratio = R / r
            if abs(ratio - round(ratio)) < 0.01:  # If close to an integer
                cycles = max(2, int(ratio)) * 2
        
        # Recreate t with appropriate cycle count for better visualization
        t = np.linspace(0, 2 * np.pi * cycles, num_points)
        
        # Update the spirograph
        x = (R - r) * np.cos(t) + d * np.cos((R - r) * t / r)
        y = (R - r) * np.sin(t) - d * np.sin((R - r) * t / r)
        
        # Update the plot
        line.set_xdata(x)
        line.set_ydata(y)
        
        # Update title with more precision for better documentation
        ax.set_title(f'Spirograph (R={R:.2f}, r={r:.2f}, d={d:.2f})')
        
        # Recalculate axis limits
        max_val = max(max(abs(x)), max(abs(y))) * 1.1
        ax.set_xlim(-max_val, max_val)
        ax.set_ylim(-max_val, max_val)
        
        fig.canvas.draw_idle()
    
    # Connect callbacks
    slider_R.on_changed(update_from_sliders)
    slider_r.on_changed(update_from_sliders)
    slider_d.on_changed(update_from_sliders)
    
    text_R.on_submit(update_from_text_R)
    text_r.on_submit(update_from_text_r)
    text_d.on_submit(update_from_text_d)
    
    # Add buttons
    save_ax = plt.axes([0.7, 0.02, 0.2, 0.05])
    save_button = Button(save_ax, 'Save High-Res Image')
    
    reset_ax = plt.axes([0.4, 0.02, 0.2, 0.05])
    reset_button = Button(reset_ax, 'Reset Values')
    
    def save(event):
        """Save a high-resolution image with current parameters"""
        # Get current values
        R = slider_R.val
        r = slider_r.val
        d = slider_d.val
        
        # Create a fresh high-resolution figure for saving
        save_fig = Figure(figsize=(10, 8), dpi=300)
        canvas = save_fig.add_subplot(111)
        
        # Calculate high-resolution version of current spirograph
        cycles = 10
        if r != 0:
            ratio = R / r
            if abs(ratio - round(ratio)) < 0.01:
                cycles = max(2, int(ratio)) * 2
                
        t_high_res = np.linspace(0, 2 * np.pi * cycles, 5000)  # More points for saving
        x = (R - r) * np.cos(t_high_res) + d * np.cos((R - r) * t_high_res / r)
        y = (R - r) * np.sin(t_high_res) - d * np.sin((R - r) * t_high_res / r)
        
        # Plot on the new figure
        canvas.plot(x, y, '-', lw=1.0)
        canvas.set_aspect('equal')
        canvas.set_axis_off()
        canvas.set_title(f'Spirograph (R={R:.2f}, r={r:.2f}, d={d:.2f})')
        
        # Set axis limits
        max_val = max(max(abs(x)), max(abs(y))) * 1.1
        canvas.set_xlim(-max_val, max_val)
        canvas.set_ylim(-max_val, max_val)
        
        # Create a descriptive filename with current parameters
        filename = f"spirograph_R{R:.2f}_r{r:.2f}_d{d:.2f}.png"
        save_fig.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"Saved as {filename}")
    
    def reset(event):
        """Reset to initial values"""
        slider_R.set_val(R_init)
        slider_r.set_val(r_init)
        slider_d.set_val(d_init)
        
        # No need to update text boxes as slider callbacks will handle it
    
    save_button.on_clicked(save)
    reset_button.on_clicked(reset)
    
    # Label section
    fig.text(0.5, 0.3, "Adjust values using sliders or type exact values in text boxes", 
             ha='center', va='center', fontsize=10)
    
    fig.text(0.2, 0.01, "R = outer circle radius, r = inner circle radius, d = pen distance from center", 
             ha='center', va='bottom', fontsize=8)
    
    plt.show()

if __name__ == "__main__":
    create_interactive_spirograph()