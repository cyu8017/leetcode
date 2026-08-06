# LeetCode 1184 - Distance Between Bus Stops
# https://leetcode.com/problems/distance-between-bus-stops/

# @param {Integer[]} distance
# @param {Integer} start
# @param {Integer} destination
# @return {Integer}
def distance_between_bus_stops(distance, start, destination)
  start, destination = destination, start if start > destination
  clockwise = distance[start...destination].sum
  [clockwise, distance.sum - clockwise].min
end
