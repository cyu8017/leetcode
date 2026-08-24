# LeetCode 3804 - Number of Centered Subarrays
# https://leetcode.com/problems/number-of-centered-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def centered_subarrays(nums)
  n = nums.length
  ans = 0
  (0...n).each do |i|
    st = {}
    s = 0
    (i...n).each do |j|
      s += nums[j]
      st[nums[j]] = true
      ans += 1 if st.key?(s)
    end
  end
  ans
end
