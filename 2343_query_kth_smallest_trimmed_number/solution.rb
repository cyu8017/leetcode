# LeetCode 2343 - Query Kth Smallest Trimmed Number
# https://leetcode.com/problems/query-kth-smallest-trimmed-number/

# @param {String[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def smallest_trimmed_numbers(nums, queries)
  n = nums.length
  m = queries.length
  ans = Array.new(m, 0)
  (0...m).each do |qi|
    k = queries[qi][0]
    trim = queries[qi][1]
    arr = []
    (0...n).each do |i|
      s = nums[i]
      arr << [s[s.length - trim..], i]
    end
    arr.sort_by! { |x| [x[0], x[1]] }
    ans[qi] = arr[k - 1][1]
  end
  ans
end
