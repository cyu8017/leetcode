# LeetCode 2980 - Check if Bitwise OR Has Trailing Zeros
# https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/

# @param {Integer[]} nums
# @return {Boolean}
def has_trailing_zeros(nums)
  even = 0
  nums.each do |v|
    if v.even?
      even += 1
      return true if even >= 2
    end
  end
  false
end
