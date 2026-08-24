# LeetCode 2841 - Maximum Sum of Almost Unique Subarray
# https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/

# @param {Integer[]} nums
# @param {Integer} m
# @param {Integer} k
# @return {Integer}
def max_sum(nums, m, k)
  freq = {}
  total = 0
  ans = 0
  nums.each_with_index do |v, i|
    freq[v] = freq.fetch(v, 0) + 1
    total += v
    if i >= k
      out = nums[i - k]
      total -= out
      c = freq.fetch(out, 0) - 1
      if c == 0
        freq.delete(out)
      else
        freq[out] = c
      end
    end
    ans = [ans, total].max if i >= k - 1 && freq.length >= m
  end
  ans
end
