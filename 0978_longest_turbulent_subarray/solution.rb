# LeetCode 0978 - Longest Turbulent Subarray
# https://leetcode.com/problems/longest-turbulent-subarray/

# @param {Integer[]} arr
# @return {Integer}
def max_turbulence_size(arr)
  ans = cur = 1
  (1...arr.length).each do |i|
    if arr[i] == arr[i - 1]
      cur = 1
    elsif i == 1 || (arr[i] - arr[i - 1]) * (arr[i - 1] - arr[i - 2]) < 0
      cur += 1
    else
      cur = 2
    end
    ans = cur if cur > ans
  end
  ans
end
