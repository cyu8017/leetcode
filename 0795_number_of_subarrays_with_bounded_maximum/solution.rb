# LeetCode 0795 - Number of Subarrays with Bounded Maximum
# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

# @param {Integer[]} nums
# @param {Integer} left
# @param {Integer} right
# @return {Integer}
def num_subarray_bounded_max(nums, left, right)
  count_at_most = lambda do |bound|
    ans = 0
    cur = 0
    nums.each do |num|
      if num <= bound
        cur += 1
        ans += cur
      else
        cur = 0
      end
    end
    ans
  end

  count_at_most.call(right) - count_at_most.call(left - 1)
end
