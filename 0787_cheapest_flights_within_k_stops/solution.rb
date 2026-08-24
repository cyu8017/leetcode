# LeetCode 0787 - Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/

# @param {Integer} n
# @param {Integer[][]} flights
# @param {Integer} src
# @param {Integer} dst
# @param {Integer} k
# @return {Integer}
def find_cheapest_price(n, flights, src, dst, k)
  dist = Array.new(n, Float::INFINITY)
  dist[src] = 0
  (k + 1).times do
    nxt = dist.dup
    flights.each do |u, v, price|
      nxt[v] = dist[u] + price if dist[u] != Float::INFINITY && dist[u] + price < nxt[v]
    end
    dist = nxt
  end
  dist[dst] == Float::INFINITY ? -1 : dist[dst].to_i
end
