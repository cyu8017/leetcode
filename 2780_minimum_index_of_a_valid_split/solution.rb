# LeetCode 2780 - Minimum Index of a Valid Split
# https://leetcode.com/problems/minimum-index-of-a-valid-split/

# @param {Integer[]} nums
# @return {Integer}
def minimum_index(nums)
  freq = Hash.new(0)
  dom = 0
  best = 0
  nums.each do |v|
    freq[v] += 1
    if freq[v] > best
      best = freq[v]
      dom = v
    end
  end
  left = 0
  n = nums.length
  (0...(n - 1)).each do |i|
    left += 1 if nums[i] == dom
    right = best - left
    return i if left * 2 > i + 1 && right * 2 > n - i - 1
  end
  -1
end
