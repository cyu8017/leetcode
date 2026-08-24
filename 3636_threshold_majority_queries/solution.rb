# LeetCode 3636 - Threshold Majority Queries
# https://leetcode.com/problems/threshold-majority-queries/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def subarray_majority(nums, queries)
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |(l, r, t), qi|
    cnt = Hash.new(0)
    (l..r).each { |i| cnt[nums[i]] += 1 }
    best = -1
    best_c = 0
    cnt.each do |v, c|
      if c >= t && (c > best_c || (c == best_c && (best == -1 || v < best)))
        best_c = c
        best = v
      end
    end
    ans[qi] = best
  end
  ans
end
