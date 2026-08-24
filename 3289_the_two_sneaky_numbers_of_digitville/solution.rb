# LeetCode 3289 - The Two Sneaky Numbers of Digitville
# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

# @param {Integer[]} nums
# @return {Integer[]}
def get_sneaky_numbers(nums)
  seen = {}
  ans = []
  nums.each do |x|
    if seen[x]
      ans << x
    else
      seen[x] = true
    end
  end
  ans
end
