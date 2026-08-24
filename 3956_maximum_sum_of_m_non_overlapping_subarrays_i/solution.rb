# LeetCode 3956 - Maximum Sum of M Non-Overlapping Subarrays I
# https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-i/

# @param {Integer[]} nums
# @param {Integer} m
# @param {Integer} l
# @param {Integer} r
# @return {Integer}
def max_sum(nums, m, l, r)
  n = nums.length
  prefix = Array.new(n + 1, 0)
  n.times { |i| prefix[i + 1] = prefix[i] + nums[i] }
  dp = Array.new(n + 1, 0)
  best_selected = -(2**62)
  (1..m).each do |_count|
    nxt = dp.dup
    deque = []
    (1..n).each do |ending|
      add_index = ending - l
      if add_index >= 0
        value = dp[add_index] - prefix[add_index]
        while !deque.empty?
          last = deque[-1]
          break if dp[last] - prefix[last] > value
          deque.pop
        end
        deque << add_index
      end
      min_index = ending - r
      deque.shift while !deque.empty? && deque[0] < min_index
      unless deque.empty?
        candidate = prefix[ending] + dp[deque[0]] - prefix[deque[0]]
        nxt[ending] = candidate if candidate > nxt[ending]
        best_selected = candidate if candidate > best_selected
      end
      nxt[ending] = nxt[ending - 1] if nxt[ending - 1] > nxt[ending]
    end
    dp = nxt
  end
  best_selected
end
