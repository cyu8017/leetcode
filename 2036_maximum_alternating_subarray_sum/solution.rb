# LeetCode 2036 - Maximum Alternating Subarray Sum
# https://leetcode.com/problems/maximum-alternating-subarray-sum/

# @param {Integer[]} nums
# @return {Integer}
def maximum_alternating_subarray_sum(nums)
  ans = -10**18
  even = 0
  nums.each_with_index do |x, i|
    if i.even?
      even += x
    else
      even = [0, even - x].max
    end
    ans = [ans, even].max
  end
  odd = 0
  (1...nums.length).each do |i|
    x = nums[i]
    if i.odd?
      odd += x
    else
      odd = [0, odd - x].max
    end
    ans = [ans, odd].max
  end
  ans
end

alias solve maximum_alternating_subarray_sum
