class Track:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return (
            str(self.__class__) + '\n' + '\n'.join(
                ('{} = {}'.format(item, self.__dict__[item])
                    for item in self.__dict__)
            )
        )


class Playlist:
    def __init__(self):
        self.tracks = []

    def enqueue(self, track):
        Playlist.__init__(self)
        self.tracks.append(str(track).split('\n'))

    # def remove(self, track_number):
    #

    # def view(self):


if __name__ == '__main__':
    myTrack = Playlist()
    n = int(input())
    for i in range(n):
        input_list = input().split(',')
        input_track = Track(input_list[0], input_list[1], input_list[2])
        myTrack.enqueue(input_track)

    # myTrack.view()
