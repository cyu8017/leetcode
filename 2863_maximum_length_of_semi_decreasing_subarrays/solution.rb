# LeetCode 2863 - Maximum Length of Semi-Decreasing Subarrays
# https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def max_subarray_length(nums)
  n = nums.length
  ans = 0
  st = []
  (0...n).each do |i|
    st << i if st.empty? || nums[i] > nums[st[-1]]
  end
  (n - 1).downto(0) do |i|
    while !st.empty? && nums[st[-1]] > nums[i]
      j = st.pop
      ans = i - j + 1 if i - j + 1 > ans
    end
  end
  ans
end
