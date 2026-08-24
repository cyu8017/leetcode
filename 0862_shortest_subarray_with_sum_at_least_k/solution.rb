# LeetCode 0862 - Shortest Subarray with Sum at Least K
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def shortest_subarray(nums, k)
  n = nums.length
  prefix = Array.new(n + 1, 0)
  nums.each_with_index { |x, i| prefix[i + 1] = prefix[i] + x }
  dq = []
  ans = n + 1
  prefix.each_with_index do |p, i|
    while !dq.empty? && p - prefix[dq[0]] >= k
      ans = [ans, i - dq.shift].min
    end
    dq.pop while !dq.empty? && p <= prefix[dq[-1]]
    dq << i
  end
  ans <= n ? ans : -1
end
