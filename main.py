import time

def divider(text):
    if text:
        length = (text.join(text)).count(text) + 1
        half = round(length/2) + 1
        print('-' * (20 - half), f'{text}', '-' * (20 - half))
        return
    print('-' * 40)


class Track:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration


class Playlist:
    def __init__(self):
        self.tracks = []

    def enqueue(self, track):
        self.tracks.append(track)

    def remove(self, track_number):
        self.tracks.remove(self.tracks[track_number - 1])

    def view(self):
        divider('VIEW')
        for index, track in enumerate(self.tracks):
            print(f'{index + 1} - {track.title} - {track.artist}')
        divider('')

    def duration(self):
        total_duration = 0
        for track in self.tracks:
            total_duration += int(track.duration)
        ty_res = time.gmtime(total_duration)
        res = time.strftime("%H:%M:%S", ty_res)
        divider('DURATION')
        print(f'Total duration: {res}')
        divider('')


if __name__ == '__main__':
    myTrack = Playlist()

    n = int(input())
    for i in range(n):
        input_list = input().split(',')
        myTrack.enqueue(Track(input_list[0], input_list[1], input_list[2]))

    myTrack.view()
    myTrack.duration()
    myTrack.remove(2)
    myTrack.view()
    myTrack.duration()
