# LeetCode 1436 - Destination City
# https://leetcode.com/problems/destination-city/

def dest_city(paths)
  starts = {}
  paths.each { |start, _| starts[start] = true }
  paths.each { |_, ending| return ending unless starts[ending] }
end
