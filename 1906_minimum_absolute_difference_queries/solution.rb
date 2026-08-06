# LeetCode 1906 - Minimum Absolute Difference Queries
# https://leetcode.com/problems/minimum-absolute-difference-queries/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def min_difference(nums, queries)
  n = nums.length
  pref = Array.new(n + 1) { Array.new(101, 0) }
  nums.each_with_index do |x, i|
    pref[i + 1] = pref[i].dup
    pref[i + 1][x] += 1
  end
  queries.map do |left, right|
    prev = -1
    best = Float::INFINITY
    (1..100).each do |value|
      if pref[right + 1][value] - pref[left][value] > 0
        best = [best, value - prev].min if prev != -1
        prev = value
      end
    end
    best == Float::INFINITY ? -1 : best
  end
end
