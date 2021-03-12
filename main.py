class Track:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration


class Playlist:
    def __init__(self):
        self.tracks = []

    def enqueue(self, track):
        self.tracks.append(f'{track.title} - {track.artist} - {track.duration}')

    # def remove(self, track_number):
    #

    def view(self):
        Playlist.__init__(self)
        print(str(self.__dict__))

    # def duration(self):

    def __str__(self):
        return (
            '\n' + '\n'.join(
                ('{} = {}'.format(item, self.__dict__[item])
                    for item in self.__dict__)
            )
        )


if __name__ == '__main__':
    myTrack = Playlist()

    n = int(input())
    for i in range(n):
        input_list = input().split(',')
        myTrack.enqueue(Track(input_list[0], input_list[1], input_list[2]))

    print(myTrack)
    # myTrack.view()
