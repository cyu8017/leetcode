# LeetCode 3523 - Make Array Non-decreasing
# https://leetcode.com/problems/make-array-non-decreasing/

# @param {Integer[]} nums
# @return {Integer}
def maximum_possible_size(nums)
  ans = 0
  mx = 0
  nums.each do |x|
    if mx <= x
      ans += 1
      mx = x
    end
  end
  ans
end
