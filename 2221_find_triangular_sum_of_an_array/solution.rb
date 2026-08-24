# LeetCode 2221 - Find Triangular Sum of an Array
# https://leetcode.com/problems/find-triangular-sum-of-an-array/

# @param {Integer[]} nums
# @return {Integer}
def triangular_sum(nums)
  while nums.length > 1
    nxt = Array.new(nums.length - 1)
    nxt.length.times { |i| nxt[i] = (nums[i] + nums[i + 1]) % 10 }
    nums = nxt
  end
  nums[0]
end
