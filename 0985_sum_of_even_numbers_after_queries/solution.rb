# LeetCode 0985 - Sum of Even Numbers After Queries
# https://leetcode.com/problems/sum-of-even-numbers-after-queries/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def sum_even_after_queries(nums, queries)
  even = nums.select { |x| x.even? }.sum
  ans = []
  queries.each do |val, i|
    even -= nums[i] if nums[i].even?
    nums[i] += val
    even += nums[i] if nums[i].even?
    ans << even
  end
  ans
end
