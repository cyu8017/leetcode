# LeetCode 3525 - Find X Value of Array II
# https://leetcode.com/problems/find-x-value-of-array-ii/

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer[][]} queries
# @return {Integer[]}
def result_array(nums, k, queries)
  n = nums.length
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, qi|
    idx, val, start, x = q[0], q[1], q[2], q[3]
    nums[idx] = val
    prod = 1
    cnt = 0
    (start...n).each do |i|
      prod = prod * (nums[i] % k) % k
      cnt += 1 if prod == x
    end
    ans[qi] = cnt
  end
  ans
end
