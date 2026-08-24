# LeetCode 2651 - Calculate Delayed Arrival Time
# https://leetcode.com/problems/calculate-delayed-arrival-time/

# @param {Integer} arrival_time
# @param {Integer} delayed_time
# @return {Integer}
def find_delayed_arrival_time(arrival_time, delayed_time)
  (arrival_time + delayed_time) % 24
end
