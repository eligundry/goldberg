import librosa

class Song:
    def __init__(self, song_path):
        self.hop_length = 1000000
        self.filename = song_path
        self.waveform, self.sample_rate = librosa.load(self.filename)

        self.tempo, self.beat_frames = librosa.beat.beat_track(y=self.waveform,
                            sr=self.sample_rate, hop_length=self.hop_length)

        self.beat_times = librosa.frames_to_time(self.beat_frames,
                                sr=self.sample_rate, hop_rate=self.hope_length)
