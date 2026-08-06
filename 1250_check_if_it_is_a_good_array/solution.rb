# LeetCode 1250 - Check If It Is a Good Array
# https://leetcode.com/problems/check-if-it-is-a-good-array/

# @param {Integer[]} nums
# @return {Boolean}
def is_good_array(nums)
  nums.reduce(:gcd) == 1
end
