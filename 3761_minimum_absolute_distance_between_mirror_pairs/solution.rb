# LeetCode 3761 - Minimum Absolute Distance Between Mirror Pairs
# https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/

# @param {Integer[]} nums
# @return {Integer}
def min_mirror_pair_distance(nums)
  reverse = lambda do |x|
    y = 0
    while x > 0
      y = y * 10 + x % 10
      x /= 10
    end
    y
  end
  n = nums.length
  pos = {}
  ans = n + 1
  nums.each_with_index do |val, i|
    ans = [ans, i - pos[val]].min if pos.key?(val)
    pos[reverse.call(val)] = i
  end
  ans > n ? -1 : ans
end
