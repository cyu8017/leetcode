# LeetCode 0218 - The Skyline Problem
# https://leetcode.com/problems/the-skyline-problem/

# @param {Integer[][]} buildings
# @return {Integer[][]}
def get_skyline(buildings)
  events = []
  buildings.each do |left, right, height|
    events << [left, -height, right]
    events << [right, 0, 0]
  end
  events.sort!

  result = []
  live = [[0, 1 << 30]]

  events.each do |x, neg_h, end_x|
    live.shift while !live.empty? && live[0][1] <= x
    live << [neg_h, end_x] if neg_h != 0
    live.sort_by! { |item| item[0] }
    height = -live[0][0]
    result << [x, height] if result.empty? || result[-1][1] != height
  end
  result
end
