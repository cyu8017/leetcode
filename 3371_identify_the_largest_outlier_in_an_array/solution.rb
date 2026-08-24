# LeetCode 3371 - Identify the Largest Outlier in an Array
# https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/

# @param {Integer[]} nums
# @return {Integer}
def get_largest_outlier(nums)
  total = 0
  freq = {}
  nums.each do |x|
    total += x
    freq[x] = (freq[x] || 0) + 1
  end
  ans = -2_147_483_648
  nums.each do |x|
    freq[x] -= 1
    rem = total - x
    if rem.even?
      cand = rem / 2
      ans = x if (freq[cand] || 0) > 0 && x > ans
    end
    freq[x] += 1
  end
  ans
end
