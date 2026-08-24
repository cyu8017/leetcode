# LeetCode 2389 - Longest Subsequence With Limited Sum
# https://leetcode.com/problems/longest-subsequence-with-limited-sum/

# @param {Integer[]} nums
# @param {Integer[]} queries
# @return {Integer[]}
def answer_queries(nums, queries)
  nums = nums.sort
  (1...nums.length).each { |i| nums[i] += nums[i - 1] }
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, i|
    lo = 0
    hi = nums.length
    while lo < hi
      mid = (lo + hi) >> 1
      if nums[mid] <= q
        lo = mid + 1
      else
        hi = mid
      end
    end
    ans[i] = lo
  end
  ans
end
