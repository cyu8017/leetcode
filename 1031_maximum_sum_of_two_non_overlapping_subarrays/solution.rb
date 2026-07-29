# LeetCode 1031 - Maximum Sum of Two Non-Overlapping Subarrays
# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

# @param {Integer[]} nums
# @param {Integer} first_len
# @param {Integer} second_len
# @return {Integer}
def max_sum_two_no_overlap(nums, first_len, second_len)
  prefix = [0]
  nums.each { |x| prefix << prefix[-1] + x }

  best = lambda do |a, b|
    best_a = ans = 0
    (a + b...prefix.length).each do |i|
      best_a = [best_a, prefix[i - b] - prefix[i - b - a]].max
      ans = [ans, best_a + prefix[i] - prefix[i - b]].max
    end
    ans
  end
  [best.call(first_len, second_len), best.call(second_len, first_len)].max
end
