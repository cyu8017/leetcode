# LeetCode 2332 - The Latest Time to Catch a Bus
# https://leetcode.com/problems/the-latest-time-to-catch-a-bus/

# @param {Integer[]} buses
# @param {Integer[]} passengers
# @param {Integer} capacity
# @return {Integer}
def latest_time_catch_the_bus(buses, passengers, capacity)
  buses = buses.sort
  passengers = passengers.sort
  pos = 0
  buses.each_with_index do |bus, bi|
    cap = capacity
    while cap > 0 && pos < passengers.length && passengers[pos] <= bus
      pos += 1
      cap -= 1
    end
    if bi == buses.length - 1
      cand = bus
      cand = passengers[pos - 1] if cap == 0
      taken = {}
      passengers.each { |p| taken[p] = true }
      cand -= 1 while taken[cand]
      return cand
    end
  end
  -1
end
