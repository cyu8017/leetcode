# LeetCode 1094 - Car Pooling
# https://leetcode.com/problems/car-pooling/

# @param {Integer[][]} trips
# @param {Integer} capacity
# @return {Boolean}
def car_pooling(trips, capacity)
  diff = Array.new(1001, 0)
  trips.each do |num, start, end_|
    diff[start] += num
    diff[end_] -= num
  end
  cur = 0
  diff.each do |x|
    cur += x
    return false if cur > capacity
  end
  true
end
