import re
import os
from pydub import AudioSegment

def edit_source(instrument, note, length):
    filename = "{}.wav".format(note)
    print(filename)
    path = "/home/junseok/jslee/capstone1/music_source/piano-raw"

    music_elem_size = 400 * length
    fullpath = os.path.join(path, filename)
    # Open file
    song = AudioSegment.from_wav(fullpath)

    # Slice audio
    # pydub uses milliseconds
    #one_min = ten_seconds * 6

    music_source = song[100:100 + music_elem_size]
    return music_source


def recons_music(freq_data, instrument):

    #instrument = 0 : piano
    reconstruct_music = AudioSegment.empty()
    #music_source = edit_source(0)
    sound_list = []
    #first = 1

    for freq in freq_data:
        #crossfade with in
        '''
        if first == 1:
            if freq >= 31.725 and freq < 63.575:
                #1st octave
                if freq >= 31.725 and freq < 33.675:
                    #c1
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 33.675 and freq < 35.67:
                    #c1#
                    reconstruct_music = reconstruct_music + music_source[1]
                elif freq >= 35.67 and freq < 37.80:
                    #d1
                    reconstruct_music = reconstruct_music + music_source[2]
                elif freq >= 37.80 and freq < 40.045:
                    #d1#
                    reconstruct_music = reconstruct_music + music_source[3]
                elif freq >= 40.045 and freq < 42.425:
                    #e1
                    reconstruct_music = reconstruct_music + music_source[4]
                elif freq >= 42.425 and freq < 44.95:
                    #f1
                    reconstruct_music = reconstruct_music + music_source[5]
                elif freq >= 44.95 and freq < 47.625:
                    #f1#
                    reconstruct_music = reconstruct_music + music_source[6]
                elif freq >= 47.625 and freq < 50.455:
                    #g1
                    reconstruct_music = reconstruct_music + music_source[7]
                elif freq >= 50.455 and freq < 53.455:
                    #g1#
                    reconstruct_music = reconstruct_music + music_source[8]
                elif freq >= 53.455 and freq < 56.635:
                    #a1
                    reconstruct_music = reconstruct_music + music_source[9]
                elif freq >= 56.635 and freq < 60.005:
                    #a1#
                    reconstruct_music = reconstruct_music + music_source[10]
                else:
                    #b1
                    reconstruct_music = reconstruct_music + music_source[11]
            elif freq >= 63.575 and freq < 127.145:
                #2nd octave
                if freq >= 63.575 and freq < 67.355:
                    #c2
                    reconstruct_music = reconstruct_music + music_source[12]
                elif freq >= 67.355 and freq < 71.36:
                    #c2#
                    reconstruct_music = reconstruct_music + music_source[13]
                elif freq >= 71.36 and freq < 75.60:
                    #d2
                    reconstruct_music = reconstruct_music + music_source[14]
                elif freq >= 75.60 and freq < 80.095:
                    #d2#
                    reconstruct_music = reconstruct_music + music_source[15]
                elif freq >= 80.095 and freq < 84.86:
                    #e2
                    reconstruct_music = reconstruct_music + music_source[16]
                elif freq >= 84.86 and freq < 89.905:
                    #f2
                    reconstruct_music = reconstruct_music + music_source[17]
                elif freq >= 89.905 and freq < 95.25:
                    #f2#
                    reconstruct_music = reconstruct_music + music_source[18]
                elif freq >= 95.35 and freq < 100.915:
                    #g2
                    reconstruct_music = reconstruct_music + music_source[19]
                elif freq >= 100.915 and freq < 106.915:
                    #g2#
                    reconstruct_music = reconstruct_music + music_source[20]
                elif freq >= 106.915 and freq < 113.27:
                    #a2
                    reconstruct_music = reconstruct_music + music_source[21]
                elif freq >= 113.27 and freq < 120.005:
                    #a2#
                    reconstruct_music = reconstruct_music + music_source[22]
                else :
                    #b2
                    reconstruct_music = reconstruct_music + music_source[23]
            elif freq >= 127.145 and freq < 254.285:
                #3rd octave
                if freq >= 127.145 and freq < 134.705:
                    #c3
                    reconstruct_music = reconstruct_music + music_source[24]
                elif freq >= 134.705 and freq < 142.71:
                    #c3#
                    reconstruct_music = reconstruct_music + music_source[25]
                elif freq >= 142.71 and freq < 151.20:
                    #d3
                    reconstruct_music = reconstruct_music + music_source[26]
                elif freq >= 151.20 and freq < 160.195:
                    #d3#
                    reconstruct_music = reconstruct_music + music_source[27]
                elif freq >= 160.195 and freq < 169.72:
                    #e3
                    reconstruct_music = reconstruct_music + music_source[28]
                elif freq >= 169.72 and freq < 179.81:
                    #f3
                    reconstruct_music = reconstruct_music + music_source[29]
                elif freq >= 179.81 and freq < 190.50:
                    #f3#
                    reconstruct_music = reconstruct_music + music_source[30]
                elif freq >= 190.50 and freq < 201.825:
                    #g3
                    reconstruct_music = reconstruct_music + music_source[31]
                elif freq >= 201.825 and freq < 213.825:
                    #g3#
                    reconstruct_music = reconstruct_music + music_source[32]
                elif freq >= 213.825 and freq < 226.54:
                    #a3
                    reconstruct_music = reconstruct_music + music_source[33]
                elif freq >= 226.54 and freq < 240.01:
                    #a3#
                    reconstruct_music = reconstruct_music + music_source[34]
                else :
                    #b3
                    reconstruct_music = reconstruct_music + music_source[35]
            elif freq >= 254.285 and freq < 508.57:
                #4th octave
                if freq >= 254.285 and freq < 269.405:
                    #c4
                    reconstruct_music = reconstruct_music + music_source[36]
                elif freq >= 269.405 and freq < 285.42:
                    #c4#
                    reconstruct_music = reconstruct_music + music_source[37]
                elif freq >= 285.42 and freq < 302.395:
                    #d4
                    reconstruct_music = reconstruct_music + music_source[38]
                elif freq >= 302.395 and freq < 320.38:
                    #d4#
                    reconstruct_music = reconstruct_music + music_source[39]
                elif freq >= 320.38 and freq < 339.43:
                    #e4
                    reconstruct_music = reconstruct_music + music_source[40]
                elif freq >= 339.43 and freq < 359.61:
                    #f4
                    reconstruct_music = reconstruct_music + music_source[41]
                elif freq >= 359.61 and freq < 380.995:
                    #f4#
                    reconstruct_music = reconstruct_music + music_source[42]
                elif freq >= 380.995 and freq < 403.65:
                    #g4
                    reconstruct_music = reconstruct_music + music_source[43]
                elif freq >= 403.65 and freq < 427.65:
                    #g4#
                    reconstruct_music = reconstruct_music + music_source[44]
                elif freq >= 427.65 and freq < 453.08:
                    #a4
                    reconstruct_music = reconstruct_music + music_source[45]
                elif freq >= 453.08 and freq < 480.02:
                    #a4#
                    reconstruct_music = reconstruct_music + music_source[46]
                else:
                    #b4
                    reconstruct_music = reconstruct_music + music_source[47]
            elif freq >= 508.57 and freq < 1017.14:
                #5th octave
                if freq >= 508.57 and freq < 538.81:
                    #c5
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 538.81 and freq < 570.84:
                    #c5#
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 570.84 and freq < 604.79:
                    #d5
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 604.79 and freq < 640.76:
                    #d5#
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 640.76 and freq < 678.86:
                    #e5
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 678.85 and freq < 719.22:
                    #f5
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 719.22 and freq < 761.99:
                    #f5#
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 761.99 and freq < 807.30:
                    #g5
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 807.30 and freq < 855.30:
                    #g5#
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 855.30 and freq < 906.16:
                    #a5
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 906.16 and freq < 960.04:
                    #a5#
                    reconstruct_music = reconstruct_music + music_source[0]
                else :
                    #b5
                    reconstruct_music = reconstruct_music + music_source[0]
            elif freq >= 1017.14 and freq < 2034.28:
                #6th octave
                if freq >= 1017.14 and freq < 1077.62:
                    #c6
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 1077.62 and freq < 1141.68:
                    #c6#
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 1141.68 and freq < 1209.58:
                    #d6
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 1209.58 and freq < 1281.52:
                    #d6#
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 1281.52 and freq < 1357.72:
                    #e6
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 1357.72 and freq < 1438.44:
                    #f6
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 1438.44 and freq < 1523.98:
                    #f6#
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 1523.98 and freq < 1614.60:
                    #g6
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 1614.60 and freq < 1710.60:
                    #g6#
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 1710.60 and freq < 1812.32:
                    #a6
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 1812.32 and freq < 1920.08:
                    #a6#
                    reconstruct_music = reconstruct_music + music_source[0]
                else :
                    #b6
                    reconstruct_music = reconstruct_music + music_source[0]
            elif freq >= 2034.28 and freq < 4061.92:
                #7th octave
                if freq >= 2034.28 and freq < 2155.24:
                    #c7
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 2155.24 and freq < 2283.36:
                    #c7#
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 2283.36 and freq < 2419.16:
                    #d7
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 2419.26 and freq < 2563.04:
                    #d7#
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 2563.04 and freq < 2715.44:
                    #e7
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 2715.44 and freq < 2876.88:
                    #f7
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 2876.88 and freq < 3047.96:
                    #f7#
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 3047.96 and freq < 3229.20:
                    #g7
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 3229.20 and freq < 3421.20:
                    #g7#
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 3421.20 and freq < 3624.64:
                    #a7
                    reconstruct_music = reconstruct_music + music_source[0]
                elif freq >= 3624.64 and freq < 3840.16:
                    #a7#
                    reconstruct_music = reconstruct_music + music_source[0]
                else :
                    #b7
                    reconstruct_music = reconstruct_music + music_source[0]
            else :
                pass
            first = 0
        else:
            if freq >= 31.725 and freq < 63.575:
                #1st octave
                if freq >= 31.725 and freq < 33.675:
                    #c1
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 33.675 and freq < 35.67:
                    #c1#
                    reconstruct_music = reconstruct_music.append(music_source[1], crossfade = 100)
                elif freq >= 35.67 and freq < 37.80:
                    #d1
                    reconstruct_music = reconstruct_music.append(music_source[2], crossfade = 100)
                elif freq >= 37.80 and freq < 40.045:
                    #d1#
                    reconstruct_music = reconstruct_music.append(music_source[3], crossfade = 100)
                elif freq >= 40.045 and freq < 42.425:
                    #e1
                    reconstruct_music = reconstruct_music.append(music_source[4], crossfade = 100)
                elif freq >= 42.425 and freq < 44.95:
                    #f1
                    reconstruct_music = reconstruct_music.append(music_source[5], crossfade = 100)
                elif freq >= 44.95 and freq < 47.625:
                    #f1#
                    reconstruct_music = reconstruct_music.append(music_source[6], crossfade = 100)
                elif freq >= 47.625 and freq < 50.455:
                    #g1
                    reconstruct_music = reconstruct_music.append(music_source[7], crossfade = 100)
                elif freq >= 50.455 and freq < 53.455:
                    #g1#
                    reconstruct_music = reconstruct_music.append(music_source[8], crossfade = 100)
                elif freq >= 53.455 and freq < 56.635:
                    #a1
                    reconstruct_music = reconstruct_music.append(music_source[9], crossfade = 100)
                elif freq >= 56.635 and freq < 60.005:
                    #a1#
                    reconstruct_music = reconstruct_music.append(music_source[10], crossfade = 100)
                else:
                    #b1
                    reconstruct_music = reconstruct_music.append(music_source[11], crossfade = 101)
            elif freq >= 63.575 and freq < 127.145:
                #2nd octave
                if freq >= 63.575 and freq < 67.355:
                    #c2
                    reconstruct_music = reconstruct_music.append(music_source[12], crossfade = 100)
                elif freq >= 67.355 and freq < 71.36:
                    #c2#
                    reconstruct_music = reconstruct_music.append(music_source[13], crossfade = 100)
                elif freq >= 71.36 and freq < 75.60:
                    #d2
                    reconstruct_music = reconstruct_music.append(music_source[14], crossfade = 100)
                elif freq >= 75.60 and freq < 80.095:
                    #d2#
                    reconstruct_music = reconstruct_music.append(music_source[15], crossfade = 100)
                elif freq >= 80.095 and freq < 84.86:
                    #e2
                    reconstruct_music = reconstruct_music.append(music_source[16], crossfade = 100)
                elif freq >= 84.86 and freq < 89.905:
                    #f2
                    reconstruct_music = reconstruct_music.append(music_source[17], crossfade = 100)
                elif freq >= 89.905 and freq < 95.25:
                    #f2#
                    reconstruct_music = reconstruct_music.append(music_source[18], crossfade = 100)
                elif freq >= 95.35 and freq < 100.915:
                    #g2
                    reconstruct_music = reconstruct_music.append(music_source[19], crossfade = 100)
                elif freq >= 100.915 and freq < 106.915:
                    #g2#
                    reconstruct_music = reconstruct_music.append(music_source[20], crossfade = 100)
                elif freq >= 106.915 and freq < 113.27:
                    #a2
                    reconstruct_music = reconstruct_music.append(music_source[21], crossfade = 100)
                elif freq >= 113.27 and freq < 120.005:
                    #a2#
                    reconstruct_music = reconstruct_music.append(music_source[22], crossfade = 100)
                else :
                    #b2
                    reconstruct_music = reconstruct_music.append(music_source[23], crossfade = 100)
            elif freq >= 127.145 and freq < 254.285:
                #3rd octave
                if freq >= 127.145 and freq < 134.705:
                    #c3
                    reconstruct_music = reconstruct_music.append(music_source[24], crossfade = 100)
                elif freq >= 134.705 and freq < 142.71:
                    #c3#
                    reconstruct_music = reconstruct_music.append(music_source[25], crossfade = 100)
                elif freq >= 142.71 and freq < 151.20:
                    #d3
                    reconstruct_music = reconstruct_music.append(music_source[26], crossfade = 100)
                elif freq >= 151.20 and freq < 160.195:
                    #d3#
                    reconstruct_music = reconstruct_music.append(music_source[27], crossfade = 100)
                elif freq >= 160.195 and freq < 169.72:
                    #e3
                    reconstruct_music = reconstruct_music.append(music_source[28], crossfade = 100)
                elif freq >= 169.72 and freq < 179.81:
                    #f3
                    reconstruct_music = reconstruct_music.append(music_source[29], crossfade = 100)
                elif freq >= 179.81 and freq < 190.50:
                    #f3#
                    reconstruct_music = reconstruct_music.append(music_source[30], crossfade = 100)
                elif freq >= 190.50 and freq < 201.825:
                    #g3
                    reconstruct_music = reconstruct_music.append(music_source[31], crossfade = 100)
                elif freq >= 201.825 and freq < 213.825:
                    #g3#
                    reconstruct_music = reconstruct_music.append(music_source[32], crossfade = 100)
                elif freq >= 213.825 and freq < 226.54:
                    #a3
                    reconstruct_music = reconstruct_music.append(music_source[33], crossfade = 100)
                elif freq >= 226.54 and freq < 240.01:
                    #a3#
                    reconstruct_music = reconstruct_music.append(music_source[34], crossfade = 100)
                else :
                    #b3
                    reconstruct_music = reconstruct_music.append(music_source[35], crossfade = 100)
            elif freq >= 254.285 and freq < 508.57:
                #4th octave
                if freq >= 254.285 and freq < 269.405:
                    #c4
                    reconstruct_music = reconstruct_music.append(music_source[36], crossfade = 100)
                elif freq >= 269.405 and freq < 285.42:
                    #c4#
                    reconstruct_music = reconstruct_music.append(music_source[37], crossfade = 100)
                elif freq >= 285.42 and freq < 302.395:
                    #d4
                    reconstruct_music = reconstruct_music.append(music_source[38], crossfade = 100)
                elif freq >= 302.395 and freq < 320.38:
                    #d4#
                    reconstruct_music = reconstruct_music.append(music_source[39], crossfade = 100)
                elif freq >= 320.38 and freq < 339.43:
                    #e4
                    reconstruct_music = reconstruct_music.append(music_source[40], crossfade = 100)
                elif freq >= 339.43 and freq < 359.61:
                    #f4
                    reconstruct_music = reconstruct_music.append(music_source[41], crossfade = 100)
                elif freq >= 359.61 and freq < 380.995:
                    #f4#
                    reconstruct_music = reconstruct_music.append(music_source[42], crossfade = 100)
                elif freq >= 380.995 and freq < 403.65:
                    #g4
                    reconstruct_music = reconstruct_music.append(music_source[43], crossfade = 100)
                elif freq >= 403.65 and freq < 427.65:
                    #g4#
                    reconstruct_music = reconstruct_music.append(music_source[44], crossfade = 100)
                elif freq >= 427.65 and freq < 453.08:
                    #a4
                    reconstruct_music = reconstruct_music.append(music_source[45], crossfade = 100)
                elif freq >= 453.08 and freq < 480.02:
                    #a4#
                    reconstruct_music = reconstruct_music.append(music_source[46], crossfade = 100)
                else:
                    #b4
                    reconstruct_music = reconstruct_music.append(music_source[47], crossfade = 100)
            elif freq >= 508.57 and freq < 1017.14:
                #5th octave
                if freq >= 508.57 and freq < 538.81:
                    #c5
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 538.81 and freq < 570.84:
                    #c5#
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 570.84 and freq < 604.79:
                    #d5
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 604.79 and freq < 640.76:
                    #d5#
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 640.76 and freq < 678.86:
                    #e5
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 678.85 and freq < 719.22:
                    #f5
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 719.22 and freq < 761.99:
                    #f5#
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 761.99 and freq < 807.30:
                    #g5
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 807.30 and freq < 855.30:
                    #g5#
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 855.30 and freq < 906.16:
                    #a5
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 906.16 and freq < 960.04:
                    #a5#
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                else :
                    #b5
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
            elif freq >= 1017.14 and freq < 2034.28:
                #6th octave
                if freq >= 1017.14 and freq < 1077.62:
                    #c6
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 1077.62 and freq < 1141.68:
                    #c6#
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 1141.68 and freq < 1209.58:
                    #d6
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 1209.58 and freq < 1281.52:
                    #d6#
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 1281.52 and freq < 1357.72:
                    #e6
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 1357.72 and freq < 1438.44:
                    #f6
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 1438.44 and freq < 1523.98:
                    #f6#
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 1523.98 and freq < 1614.60:
                    #g6
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 1614.60 and freq < 1710.60:
                    #g6#
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 1710.60 and freq < 1812.32:
                    #a6
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 1812.32 and freq < 1920.08:
                    #a6#
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                else :
                    #b6
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
            elif freq >= 2034.28 and freq < 4061.92:
                #7th octave
                if freq >= 2034.28 and freq < 2155.24:
                    #c7
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 2155.24 and freq < 2283.36:
                    #c7#
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 2283.36 and freq < 2419.16:
                    #d7
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 2419.26 and freq < 2563.04:
                    #d7#
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 2563.04 and freq < 2715.44:
                    #e7
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 2715.44 and freq < 2876.88:
                    #f7
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 2876.88 and freq < 3047.96:
                    #f7#
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 3047.96 and freq < 3229.20:
                    #g7
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 3229.20 and freq < 3421.20:
                    #g7#
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 3421.20 and freq < 3624.64:
                    #a7
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                elif freq >= 3624.64 and freq < 3840.16:
                    #a7#
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
                else :
                    #b7
                    reconstruct_music = reconstruct_music.append(music_source[0], crossfade = 100)
            else :
                pass
        #out of range
        '''
        #crossfade with in
        if freq >= 31.725 and freq < 63.575:
            #1st octave
            if freq >= 31.725 and freq < 33.675:
                #c1
                sound_list.append([1,0])
            elif freq >= 33.675 and freq < 35.67:
                #c1#
                sound_list.append([1,1])
            elif freq >= 35.67 and freq < 37.80:
                #d1
                sound_list.append([1,2])
            elif freq >= 37.80 and freq < 40.045:
                #d1#
                sound_list.append([1,3])
            elif freq >= 40.045 and freq < 42.425:
                #e1
                sound_list.append([1,4])
            elif freq >= 42.425 and freq < 44.95:
                #f1
                sound_list.append([1,5])
            elif freq >= 44.95 and freq < 47.625:
                #f1#
                sound_list.append([1,6])
            elif freq >= 47.625 and freq < 50.455:
                #g1
                sound_list.append([1,7])
            elif freq >= 50.455 and freq < 53.455:
                #g1#
                sound_list.append([1,8])
            elif freq >= 53.455 and freq < 56.635:
                #a1
                sound_list.append([1,9])
            elif freq >= 56.635 and freq < 60.005:
                #a1#
                sound_list.append([1,10])
            else:
                #b1
                sound_list.append([1,11])
        elif freq >= 63.575 and freq < 127.145:
            #2nd octave
            if freq >= 63.575 and freq < 67.355:
                #c2
                sound_list.append([2,0])
            elif freq >= 67.355 and freq < 71.36:
                #c2#
                sound_list.append([2,1])
            elif freq >= 71.36 and freq < 75.60:
                #d2
                sound_list.append([2,2])
            elif freq >= 75.60 and freq < 80.095:
                #d2#
                sound_list.append([2,3])
            elif freq >= 80.095 and freq < 84.86:
                #e2
                sound_list.append([2,4])
            elif freq >= 84.86 and freq < 89.905:
                #f2
                sound_list.append([2,5])
            elif freq >= 89.905 and freq < 95.25:
                #f2#
                sound_list.append([2,6])
            elif freq >= 95.35 and freq < 100.915:
                #g2
                sound_list.append([2,7])
            elif freq >= 100.915 and freq < 106.915:
                #g2#
                sound_list.append([2,8])
            elif freq >= 106.915 and freq < 113.27:
                #a2
                sound_list.append([2,9])
            elif freq >= 113.27 and freq < 120.005:
                #a2#
                sound_list.append([2,10])
            else :
                #b2
                sound_list.append([2,11])
        elif freq >= 127.145 and freq < 254.285:
            #3rd octave
            if freq >= 127.145 and freq < 134.705:
                #c3
                sound_list.append([3,0])
            elif freq >= 134.705 and freq < 142.71:
                #c3#
                sound_list.append([3,1])
            elif freq >= 142.71 and freq < 151.20:
                #d3
                sound_list.append([3,2])
            elif freq >= 151.20 and freq < 160.195:
                #d3#
                sound_list.append([3,3])
            elif freq >= 160.195 and freq < 169.72:
                #e3
                sound_list.append([3,4])
            elif freq >= 169.72 and freq < 179.81:
                #f3
                sound_list.append([3,5])
            elif freq >= 179.81 and freq < 190.50:
                #f3#
                sound_list.append([3,6])
            elif freq >= 190.50 and freq < 201.825:
                #g3
                sound_list.append([3,7])
            elif freq >= 201.825 and freq < 213.825:
                #g3#
                sound_list.append([3,8])
            elif freq >= 213.825 and freq < 226.54:
                #a3
                sound_list.append([3,9])
            elif freq >= 226.54 and freq < 240.01:
                #a3#
                sound_list.append([3,10])
            else :
                #b3
                sound_list.append([3,11])
        elif freq >= 254.285 and freq < 508.57:
            #4th octave
            if freq >= 254.285 and freq < 269.405:
                #c4
                sound_list.append([4,0])
            elif freq >= 269.405 and freq < 285.42:
                #c4#
                sound_list.append([4,1])
            elif freq >= 285.42 and freq < 302.395:
                #d4
                sound_list.append([4,2])
            elif freq >= 302.395 and freq < 320.38:
                #d4#
                sound_list.append([4,3])
            elif freq >= 320.38 and freq < 339.43:
                #e4
                sound_list.append([4,4])
            elif freq >= 339.43 and freq < 359.61:
                #f4
                sound_list.append([4,5])
            elif freq >= 359.61 and freq < 380.995:
                #f4#
                sound_list.append([4,6])
            elif freq >= 380.995 and freq < 403.65:
                #g4
                sound_list.append([4,7])
            elif freq >= 403.65 and freq < 427.65:
                #g4#
                sound_list.append([4,8])
            elif freq >= 427.65 and freq < 453.08:
                #a4
                sound_list.append([4,9])
            elif freq >= 453.08 and freq < 480.02:
                #a4#
                sound_list.append([4,10])
            else:
                #b4
                sound_list.append([4,11])
        elif freq >= 508.57 and freq < 1017.14:
            #5th octave
            if freq >= 508.57 and freq < 538.81:
                #c5
                sound_list.append([5,0])
            elif freq >= 538.81 and freq < 570.84:
                #c5#
                sound_list.append([5,1])
            elif freq >= 570.84 and freq < 604.79:
                #d5
                sound_list.append([5,2])
            elif freq >= 604.79 and freq < 640.76:
                #d5#
                sound_list.append([5,3])
            elif freq >= 640.76 and freq < 678.86:
                #e5
                sound_list.append([5,4])
            elif freq >= 678.85 and freq < 719.22:
                #f5
                sound_list.append([5,5])
            elif freq >= 719.22 and freq < 761.99:
                #f5#
                sound_list.append([5,6])
            elif freq >= 761.99 and freq < 807.30:
                #g5
                sound_list.append([5,7])
            elif freq >= 807.30 and freq < 855.30:
                #g5#
                sound_list.append([5,8])
            elif freq >= 855.30 and freq < 906.16:
                #a5
                sound_list.append([5,9])
            elif freq >= 906.16 and freq < 960.04:
                #a5#
                sound_list.append([5,10])
            else :
                #b5
                sound_list.append([5,11])
        elif freq >= 1017.14 and freq < 2034.28:
            #6th octave
            if freq >= 1017.14 and freq < 1077.62:
                #c6
                sound_list.append([6,0])
            elif freq >= 1077.62 and freq < 1141.68:
                #c6#
                sound_list.append([6,1])
            elif freq >= 1141.68 and freq < 1209.58:
                #d6
                sound_list.append([6,2])
            elif freq >= 1209.58 and freq < 1281.52:
                #d6#
                sound_list.append([6,3])
            elif freq >= 1281.52 and freq < 1357.72:
                #e6
                sound_list.append([6,4])
            elif freq >= 1357.72 and freq < 1438.44:
                #f6
                sound_list.append([6,5])
            elif freq >= 1438.44 and freq < 1523.98:
                #f6#
                sound_list.append([6,6])
            elif freq >= 1523.98 and freq < 1614.60:
                #g6
                sound_list.append([6,7])
            elif freq >= 1614.60 and freq < 1710.60:
                #g6#
                sound_list.append([6,8])
            elif freq >= 1710.60 and freq < 1812.32:
                #a6
                sound_list.append([6,9])
            elif freq >= 1812.32 and freq < 1920.08:
                #a6#
                sound_list.append([6,10])
            else :
                #b6
                sound_list.append([6,11])
        elif freq >= 2034.28 and freq < 4061.92:
            #7th octave
            if freq >= 2034.28 and freq < 2155.24:
                #c7
                sound_list.append([7,0])
            elif freq >= 2155.24 and freq < 2283.36:
                #c7#
                sound_list.append([7,1])
            elif freq >= 2283.36 and freq < 2419.16:
                #d7
                sound_list.append([7,2])
            elif freq >= 2419.26 and freq < 2563.04:
                #d7#
                sound_list.append([7,3])
            elif freq >= 2563.04 and freq < 2715.44:
                #e7
                sound_list.append([7,4])
            elif freq >= 2715.44 and freq < 2876.88:
                #f7
                sound_list.append([7,5])
            elif freq >= 2876.88 and freq < 3047.96:
                #f7#
                sound_list.append([7,6])
            elif freq >= 3047.96 and freq < 3229.20:
                #g7
                sound_list.append([7,7])
            elif freq >= 3229.20 and freq < 3421.20:
                #g7#
                sound_list.append([7,8])
            elif freq >= 3421.20 and freq < 3624.64:
                #a7
                sound_list.append([7,9])
            elif freq >= 3624.64 and freq < 3840.16:
                #a7#
                sound_list.append([7,10])
            else :
                #b7
                sound_list.append([7,11])
        else :
            pass

    temp_list = [0,0,0]
    first_source = True
    for sound in sound_list:
        print("{}octave".format(sound[0]))
        if first_source == True:
            temp_list = [sound[0], sound[1], 1]
            first_source = False
        else:
            if sound is not sound_list[-1]:
                if temp_list[0] != sound[0] or temp_list[1] != sound[1]:
                    note = temp_list[0] * 100 + temp_list[1]
                    reconstruct_music = reconstruct_music + edit_source(0, note, temp_list[2])
                    temp_list[0] = sound[0]
                    temp_list[1] = sound[1]
                    temp_list[2] = 1
                else:
                    temp_list[2] = temp_list[2] + 1
            else:
                if temp_list[0] != sound[0] or temp_list[1] != sound[1]:
                    note = temp_list[0] * 100 + temp_list[1]
                    reconstruct_music = reconstruct_music + edit_source(0, note, temp_list[2])
                    note = sound[0] * 100 + sound[1]
                    reconstruct_music = reconstruct_music + edit_source(0, note, 1)
                else:
                    temp_list[2] = temp_list[2] + 1
                    note = temp_list[0] * 100 + temp_list[1]
                    reconstruct_music = reconstruct_music + edit_source(0, note, temp_list[2])
               

    #reconstruct_music.overlay(reconstruct_music, 100)
    reconstruct_music.export('new_music.wav', format='wav')
