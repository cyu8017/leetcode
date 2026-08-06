# LeetCode 1960 - Maximum Product of the Length of Two Palindromic Substrings
# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/

# @param {String} s
# @return {Integer}
def max_product(s)
  n = s.length
  radius = Array.new(n, 0)
  center = right = 0
  n.times do |i|
    radius[i] = [right - i, radius[2 * center - i]].min if i < right
    while i - radius[i] - 1 >= 0 && i + radius[i] + 1 < n && s[i - radius[i] - 1] == s[i + radius[i] + 1]
      radius[i] += 1
    end
    if i + radius[i] > right
      center = i
      right = i + radius[i]
    end
  end
  end_arr = Array.new(n, 1)
  start = Array.new(n, 1)
  n.times do |i|
    r = radius[i]
    end_arr[i + r] = [end_arr[i + r], 2 * r + 1].max
    start[i - r] = [start[i - r], 2 * r + 1].max
  end
  (n - 2).downto(0) { |i| end_arr[i] = [end_arr[i], end_arr[i + 1] - 2].max }
  (1...n).each { |i| start[i] = [start[i], start[i - 1] - 2].max }
  pre = Array.new(n, 0)
  pre[0] = end_arr[0]
  (1...n).each { |i| pre[i] = [pre[i - 1], end_arr[i]].max }
  suf = Array.new(n, 0)
  suf[-1] = start[-1]
  (n - 2).downto(0) { |i| suf[i] = [suf[i + 1], start[i]].max }
  (0...n - 1).map { |i| pre[i] * suf[i + 1] }.max
end
