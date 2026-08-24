# LeetCode 3511 - Make a Positive Array
# https://leetcode.com/problems/make-a-positive-array/

# @param {Integer[]} nums
# @return {Integer}
def make_array_positive(nums)
  ans = 0
  l = -1
  pre_mx = 0
  s = 0
  (0...nums.length).each do |r|
    s += nums[r]
    if r - l > 2 && s <= pre_mx
      ans += 1
      l = r
      pre_mx = 0
      s = 0
    elsif r - l >= 2
      pre_mx = [pre_mx, s - nums[r] - nums[r - 1]].max
    end
  end
  ans
end
