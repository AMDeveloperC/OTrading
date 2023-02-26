from DataProvider import OnlineTrading
import math
import random

class ReservationPricing(OnlineTrading):
    def reservation_pricing(self):
        self.reservation = math.sqrt(self.phi) * self.minimum
        while (self.days_left > 1):
            if (self.get_next() >= self.reservation):
                self.buy()
        self.buy()
        self.approximation = math.sqrt(self.phi)

    # Quest'algoritmo sceglie il reservation pricing a caso in un intervallo suddiviso in potenze di due
    # k deve essere un intero positivo maggiore o uguale di zero, quindi lo scegli come logaritmo
    def randomized_reservation_pricing(self, epsilon = 0.45):
        self.positive_integer = math.log(self.phi, 1 + epsilon)
        i = random.randrange(0, int(self.positive_integer))
        print("i = ", i)
        self.reservation = pow(2, i) * self.minimum
        print("Reservation = ", self.reservation)
        while(self.days_left > 1):
            if(self.get_next() >= self.reservation):
                self.buy()
        self.buy()
        self.approximation = math.sqrt(self.phi)
