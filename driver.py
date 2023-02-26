from reservationPricing import ReservationPricing

G = ReservationPricing()
G.reservation_pricing()
print("We got: ", G.max_found)
print("Opt:    ", G.maximum)
print("min:    ", G.minimum)
print("phi:    ", G.phi)
print("approximation:    ", G.approximation)