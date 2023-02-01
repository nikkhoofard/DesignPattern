class Cinema:
    pass


class Movie:
    pass


class Time:
    pass


class Hall:
    def __init__(self, name, cinema, capacity):
        self.cinema = cinema
        self.capacity = capacity
        self.name = name


class Seat:
    def __init__(self, number):
        self.number = number
        self.status = None
        self.customer = None


class Sens:
    def __init__(self, cinema, movie, time, hall):
        self.cinema = cinema
        self.movie = movie
        self.time = time
        self.hall = hall
        self.seats = list()
        self.prototype_seats()

    def prototype_seats(self):
        """Prototype all seat of selected hall"""
        for i in range(self.hall.capacity):
            self.seats.append(Seat(i))


if __name__ == "__main__":
    cinema = Cinema()
    movie = Movie()
    time = Time()
    hall = Hall('Hall name', cinema, 39)

    sens = Sens(cinema, movie, time, hall)
    print(len(sens.seats))
    print(type(sens.seats[0]))