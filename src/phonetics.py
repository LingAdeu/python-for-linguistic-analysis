import numpy as np
import matplotlib.pyplot as plt
import parselmouth

# function for drawing spectogram
def draw_spectrogram(spectrogram, dynamic_range=70):
    X, Y = spectrogram.x_grid(), spectrogram.y_grid()
    sg_db = 10 * np.log10(spectrogram.values)
    plt.pcolormesh(X, Y, sg_db, vmin=sg_db.max() - dynamic_range, cmap='afmhot')
    plt.ylim([spectrogram.ymin, spectrogram.ymax])
    plt.xlabel("time [s]")
    plt.ylabel("frequency [Hz]")

# function for drawing pitch
def draw_pitch(pitch):
    pitch_values = pitch.selected_array['frequency']
    pitch_values[pitch_values==0] = np.nan
    # plt.plot(pitch.xs(), pitch_values, 'o', markersize=6, color='white', label='_nolegend_')
    # plt.plot(pitch.xs(), pitch_values, 'o', markersize=3)
    plt.plot(pitch.xs(), pitch_values, linewidth=4, color='white', label='_nolegend_')
    plt.plot(pitch.xs(), pitch_values, linewidth=2, color='red')
    plt.grid(False)
    plt.ylim(0, pitch.ceiling)
    plt.ylabel("fundamental frequency [Hz]")
    plt.legend(['pitch'])

# function for drawing intensity
def draw_intensity(intensity):
    plt.plot(intensity.xs(), intensity.values.T, linewidth=4, color='white', label='_nolegend_')
    plt.plot(intensity.xs(), intensity.values.T, linewidth=2, color='blue')
    plt.grid(False)
    plt.ylim(0)
    plt.ylabel("intensity [dB]")
    plt.legend(['intensity'])