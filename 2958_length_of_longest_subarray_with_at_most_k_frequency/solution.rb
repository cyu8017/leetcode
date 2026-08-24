# LeetCode 2958 - Length of Longest Subarray With at Most K Frequency
# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_subarray_length(nums, k)
  freq = Hash.new(0)
  ans = 0
  left = 0
  nums.each_with_index do |v, right|
    freq[v] += 1
    while freq[v] > k
      freq[nums[left]] -= 1
      left += 1
    end
    ans = right - left + 1 if right - left + 1 > ans
  end
  ans
end
