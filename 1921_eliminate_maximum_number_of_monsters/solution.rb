# LeetCode 1921 - Eliminate Maximum Number of Monsters
# https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

# @param {Integer[]} dist
# @param {Integer[]} speed
# @return {Integer}
def eliminate_maximum(dist, speed)
  arrival = dist.each_with_index.map { |d, i| (d + speed[i] - 1) / speed[i] }.sort
  arrival.each_with_index do |t, i|
    return i if t <= i
  end
  arrival.length
end
