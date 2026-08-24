# LeetCode 3892 - Minimum Operations to Achieve At Least K Peaks
# https://leetcode.com/problems/minimum-operations-to-achieve-at-least-k-peaks/

INF3892 = (1 << 53) / 4

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_operations(nums, k)
  n = nums.length
  return 0 if k == 0
  return -1 if k > n / 2
  cost = Array.new(n, 0)
  n.times do |i|
    left = nums[(i + n - 1) % n]
    right = nums[(i + 1) % n]
    need = [left, right].max
    cost[i] = need - nums[i] + 1 if need >= nums[i]
  end
  line = lambda do |left, right, choose|
    return 0 if choose == 0
    return INF3892 if left > right || choose > (right - left + 2) / 2
    prev2 = Array.new(choose + 1, INF3892)
    prev1 = Array.new(choose + 1, INF3892)
    prev2[0] = prev1[0] = 0
    (left..right).each do |i|
      current = prev1.dup
      (1..choose).each do |j|
        if prev2[j - 1] != INF3892 && prev2[j - 1] + cost[i] < current[j]
          current[j] = prev2[j - 1] + cost[i]
        end
      end
      prev2 = prev1
      prev1 = current
    end
    prev1[choose]
  end
  answer = line.call(1, n - 1, k)
  with_first = line.call(2, n - 2, k - 1)
  if with_first != INF3892
    with_first += cost[0]
    answer = [answer, with_first].min
  end
  return -1 if answer == INF3892
  answer
end
