# -*- coding: utf-8 -*-

DEBUG = False

SAVEDIR = "c:\\temp"  # folder where to save the recordings
BUFFER = 0.1  # time to buffer audio input
PIDFILE = "c:\\temp\\mumblerecbot.pid"  # location to store the process id

HOST = "localhost"  # murmur server
PORT = 64738  # murmur port
USER = "recorder"  # mumur user
PASSWORD = "recorder"  # mumur user
CHANNEL = ""  # channel to move in ("" = root)

USER_COUNT = 2  # start to record with how many connected users (recorder not included)

# Create a stereo difference based on the channel the user is in, when playing with teams taht can't ear each other
# region is the same for the subtitle webvtt file
STEREO_CHANNELS = {"Team 1": {"stereo": (1, 0), "region": "left"},
                   "Team 2": {"stereo": (0, 1), "region": "right"},
                   "Team 3": {"stereo": (1, 0), "region": "left"},
                   "Team 4": {"stereo": (0, 1), "region": "right"}}

# some constants
BITRATE = 48000
RESOLUTION = 10 # in ms
FLOAT_RESOLUTION = float(RESOLUTION) / 1000
MONO_CHUNK_SIZE = BITRATE * 2 * RESOLUTION / 1000
STEREO_CHUNK_SIZE = MONO_CHUNK_SIZE * 2 

ENCODER = "oggenc2 --raw --raw-bits=16 --raw-chan=2 --raw-rate=48000 --quality=4 --quiet -o %s.ogg -"  # command to send the audio in a pipe for external encoding

# comment to be shown in mumble for the recorder user
COMMENT_SUFFIX = "<br>/start:forced" + \
                 "<br>/stop:blocked" + \
                 "<br>/auto[=x]:Automatic start-stop (when x users connected)" + \
                 "<br>/newfile:new audio file" + \
                 "<br>/exit:disconnect" + \
                 "<br>/gamestart:Create a game chapter" + \
                 "<br>/gamestop:Finish a game chapter" 

# The user's avater is used to see if it is recording in the overlay
START_BITMAP = "start.png"
STOP_BITMAP = "stop.png"

# prevent to create multiple chapters too fast
CHAPTER_MIN_INTERVAL = 10
