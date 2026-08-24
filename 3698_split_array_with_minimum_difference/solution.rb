# LeetCode 3698 - Split Array With Minimum Difference
# https://leetcode.com/problems/split-array-with-minimum-difference/

# @param {Integer[]} nums
# @return {Integer}
def split_array(nums)
  n = nums.length
  s = Array.new(n, 0)
  f = Array.new(n, true)
  g = Array.new(n, true)
  s[0] = nums[0]
  (1...n).each do |i|
    s[i] = s[i - 1] + nums[i]
    f[i] = f[i - 1]
    f[i] = false if nums[i] <= nums[i - 1]
  end
  (n - 2).downto(0) do |i|
    g[i] = g[i + 1]
    g[i] = false if nums[i] <= nums[i + 1]
  end
  inf = 10**18
  ans = inf
  (0...(n - 1)).each do |i|
    next unless f[i] && g[i + 1]

    s1 = s[i]
    s2 = s[n - 1] - s[i]
    d = (s1 - s2).abs
    ans = d if d < ans
  end
  ans < inf ? ans : -1
end
