# LeetCode 0992 - Subarrays with K Different Integers
# https://leetcode.com/problems/subarrays-with-k-different-integers/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def subarrays_with_k_distinct(nums, k)
  at_most = lambda do |m|
    count = Hash.new(0)
    left = ans = 0
    nums.each_with_index do |x, right|
      count[x] += 1
      while count.length > m
        count[nums[left]] -= 1
        count.delete(nums[left]) if count[nums[left]].zero?
        left += 1
      end
      ans += right - left + 1
    end
    ans
  end
  at_most.call(k) - at_most.call(k - 1)
end
