import sys
import numpy as np
#import wavefile         # pip install wavefile (dependency: libsndfile)
import pysndfile         # pip install pysndfile (dependency: libsndfile)
import plotext as plx    # pip install plotext


def plot(data, fs, start=0, dur=None, plot_height=10, color="blue", marker="small", canvas_color="black", ticks_color="iron", grid=True):
    """Plots data to the console using plotext, with several parameters for formating


    """

    data = np.atleast_2d(data)

    start_samp = int(start * fs)

    if dur != None:
        end_samp = int(min((start + dur) * fs, data.size))
    else:
        end_samp = data.size

    n = end_samp - start_samp
    x = np.linspace(start_samp, end_samp, int(n)) / fs
    ylim = np.max(data[start_samp:end_samp, :])

    for channel in range(data.shape[1]):

        plx.plot(x, data[start_samp:end_samp, channel], color = color, marker = marker)
        plx.plotsize(None,plot_height)
        plx.canvas_color(canvas_color)
        plx.axes_color(canvas_color)
        plx.ticks_color(ticks_color)
        if data.shape[1] > 1: 
            plx.ylabel(f"Channel {channel+1}")
        plx.xlabel(f"Time (s)")
        plx.grid(grid)
        plx.ylim(-ylim, ylim)

        plx.show()
        plx.clear_data()


def main():
    """This is the function called when run at the command line


    """

    if len(sys.argv) == 1:
        print("Usage: audioview /path/to/audio/file [start_s] [dur_s]")

    else:
        filename = sys.argv[1]
        data, fs, enc_ = pysndfile.sndio.read(filename) #, force_2d=True)
        start = 0
        dur = None
        if len(sys.argv) > 2:
            start = float(sys.argv[2])
            if len(sys.argv) > 3:
                dur = float(sys.argv[3])
        plot(data,fs, start=start, dur=dur)


if __name__ == "__main__":
    main()
