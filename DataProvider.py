import urllib.request

# https://data.nasdaq.com/tools/api

class OnlineTrading:
    """
    It allows to download data from nasdaq officials dataset
    It requires to specify the topic to investigate and the time range
    """
    def __init__(self, key = "OPEC", table = "ORB", start_date = "2003-01-01", end_date = "2003-03-06", verbose = False):
        self.max_found = 0.0
        self.verbose = verbose

        url = "https://data.nasdaq.com/api/v3/datasets/"+str(key)+"/"+str(table)
        url += ".csv?"
        url += "start_date="+str(start_date)
        url += "&end_date="+str(end_date)

        downloaded_data = urllib.request.urlopen(url)
        self.data_set = downloaded_data.readlines()
        self.data_set = self.data_set[1:]
        self.data_set.reverse()
        self.last_value = 0.0
        self.last_day = -1
        self.canbuy = True
        self.days_left = len(self.data_set)

        self.minimum = float('inf')
        self.maximum = 0
        for line in self.data_set:
            split_line = line.decode('utf8').strip('\n').split(',')
            self.minimum = min(self.minimum, float(split_line[1]))
            self.maximum = max(self.maximum, float(split_line[1]))
        self.phi = self.maximum / self.minimum

    def get_next(self):
        if self.days_left == 0:
            return 0

        self.days_left -= 1
        self.last_day += 1
        split_line = self.data_set[self.last_day].decode('utf8').split(',')
        if self.verbose:
            print(split_line)
            print("Value: ", float(split_line[1]))
        self.last_value = float(split_line[1])

        return float(split_line[1])
        
    def buy(self):
        if self.canbuy:
            self.max_found = self.last_value
            self.canbuy = False
