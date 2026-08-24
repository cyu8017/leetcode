# LeetCode 3897 - Maximum Value of Concatenated Binary Segments
# https://leetcode.com/problems/maximum-value-of-concatenated-binary-segments/

MOD3897 = 1_000_000_007

def group3897(p)
  return 0 if p[1] == 0
  p[0] > 0 ? 1 : 2
end

# @param {Integer[]} nums1
# @param {Integer[]} nums0
# @return {Integer}
def max_value(nums1, nums0)
  n = nums1.length
  pairs = n.times.map { |i| [nums1[i], nums0[i]] }
  b = 0
  n.times { |i| b += nums1[i] + nums0[i] }
  pairs.sort_by! do |a|
    g = group3897(a)
    second = if g == 0
               -a[0]
             elsif g == 1
               -a[0]
             else
               a[1]
             end
    third = g == 1 ? a[1] : 0
    [g, second, third]
  end
  p = Array.new(b, 0)
  p[0] = 1
  (1...b).each { |i| p[i] = (2 * p[i - 1]) % MOD3897 }
  ans = 0
  b -= 1
  pairs.each do |pr|
    cnt1, cnt0 = pr[0], pr[1]
    while cnt1 > 0
      ans = (ans + p[b]) % MOD3897
      b -= 1
      cnt1 -= 1
    end
    b -= cnt0
  end
  ans
end
