# LeetCode 2461 - Maximum Sum of Distinct Subarrays With Length K
# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_subarray_sum(nums, k)
  cnt = Hash.new(0)
  total = 0
  ans = 0
  nums.each_with_index do |x, i|
    total += x
    cnt[x] += 1
    if i >= k
      y = nums[i - k]
      total -= y
      c = cnt[y] - 1
      if c == 0
        cnt.delete(y)
      else
        cnt[y] = c
      end
    end
    ans = total if i >= k - 1 && cnt.length == k && total > ans
  end
  ans
end
