# LeetCode 2731 - Movement of Robots
# https://leetcode.com/problems/movement-of-robots/

# @param {Integer[]} nums
# @param {String} s
# @param {Integer} d
# @return {Integer}
def sum_distance(nums, s, d)
  mod = 1_000_000_007
  n = nums.length
  pos = (0...n).map { |i| nums[i] + (s[i] == "R" ? d : -d) }
  pos.sort!
  ans = 0
  pref = 0
  (0...n).each do |i|
    ans = (ans + ((pos[i] * i - pref) % mod + mod) % mod) % mod
    pref += pos[i]
  end
  (ans % mod + mod) % mod
end
