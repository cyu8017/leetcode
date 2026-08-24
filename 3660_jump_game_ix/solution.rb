# LeetCode 3660 - Jump Game IX
# https://leetcode.com/problems/jump-game-ix/

# @param {Integer[]} nums
# @return {Integer[]}
def max_value(nums)
  n = nums.length
  ans = Array.new(n, 0)
  pre_max = Array.new(n, 0)
  pre_max[0] = nums[0]
  (1...n).each { |i| pre_max[i] = [pre_max[i - 1], nums[i]].max }
  suf_min = 1073741823
  (n - 1).downto(0) do |i|
    ans[i] = pre_max[i] > suf_min ? ans[i + 1] : pre_max[i]
    suf_min = nums[i] if nums[i] < suf_min
  end
  ans
end
