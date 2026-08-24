# LeetCode 2832 - Maximal Range That Each Element Is Maximum in It
# https://leetcode.com/problems/maximal-range-that-each-element-is-maximum-in-it/

# @param {Integer[]} nums
# @return {Integer[]}
def maximum_length(nums)
  n = nums.length
  left = Array.new(n, 0)
  right = Array.new(n, 0)
  st = []
  (0...n).each do |i|
    while !st.empty? && nums[st[-1]] < nums[i]
      st.pop
    end
    left[i] = st.empty? ? -1 : st[-1]
    st << i
  end
  st.clear
  (n - 1).downto(0) do |i|
    while !st.empty? && nums[st[-1]] <= nums[i]
      st.pop
    end
    right[i] = st.empty? ? n : st[-1]
    st << i
  end
  (0...n).map { |i| right[i] - left[i] - 1 }
end
