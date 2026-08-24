# LeetCode 3074 - Apple Redistribution into Boxes
# https://leetcode.com/problems/apple-redistribution-into-boxes/

# @param {Integer[]} apple
# @param {Integer[]} capacity
# @return {Integer}
def minimum_boxes(apple, capacity)
  capacity.sort!
  s = apple.sum
  i = 1
  loop do
    s -= capacity[capacity.length - i]
    return i if s <= 0
    i += 1
  end
end
