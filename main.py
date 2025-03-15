import json
from collections import defaultdict
from queue import PriorityQueue

class Solution:
    def CheapestFLight(self, n, flights, src, dst, k):
        adj = defaultdict(list)

        for flightdata in flights:
            start, end, price = flightdata
            adj[start].append([end, price])

        del flightdata
        pq = PriorityQueue()
        dist = defaultdict(lambda: float("inf"))
        pq.put((0, 0, src))
        result = float("inf")

        while not pq.empty():
            stop, price, start = pq.get()
            for sub_data in adj[start]:
                sub, sub_price = sub_data
                local_price = sub_price + price
                if stop <= k and dist[sub] > local_price:
                    if sub == dst:
                        result = min(result, price + sub_price)
                    dist[sub] = local_price
                    pq.put((stop + 1, local_price, sub))

        return result if result != float("inf") else -1

def load_json_input(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

file_path = "flight_data.json"
input_data = load_json_input(file_path)

n = input_data["n"]
flights = input_data["flights"]
src = input_data["src"]
dst = input_data["dst"]
k = input_data["k"]

obj = Solution()
result = obj.CheapestFLight(n, flights, src, dst, k)

print("Cheapest Flight Cost:", result)
