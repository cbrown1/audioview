import sys
import numpy as np
#import wavefile         # pip install wavefile (dependency: libsndfile)
import pysndfile         # pip install pysndfile (dependency: libsndfile)
import plotext as plx    # pip install plotext


def plot(data, fs, plot_height=10, color="blue", marker="small", canvas_color="black", ticks_color="iron", grid=True):

    x = np.linspace(0, data.size/fs, data.size)
    mx = np.max(data)

    for channel in range(data.shape[1]):

        plx.plot(x, data[:, channel], color = color, marker = marker)
        plx.plotsize(None,plot_height)
        plx.canvas_color(canvas_color)
        plx.axes_color(canvas_color)
        plx.ticks_color(ticks_color)
        if data.shape[1] > 1: 
            plx.ylabel(f"Channel {channel+1}")
        plx.xlabel(f"Time (s)")
        plx.grid(grid)
        plx.ylim(-mx, mx)

        plx.show()
        plx.clear_data()


def main():

    if len(sys.argv) == 1:
        print("Usage: audioview /path/to/audio/file")

    else:
        filename = sys.argv[1]

        data, fs, enc_ = pysndfile.sndio.read(filename, force_2d=True)

    plot(data,fs)


if __name__ == "__main__":
    main()
