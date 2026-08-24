# LeetCode 3883 - Count Non Decreasing Arrays With Given Digit Sums
# https://leetcode.com/problems/count-non-decreasing-arrays-with-given-digit-sums/

# @param {Integer[]} digit_sum
# @return {Integer}
def count_non_decreasing_arrays(digit_sum)
  mod = 1_000_000_007
  groups = Array.new(51) { [] }
  (0..5000).each do |x|
    s = 0
    y = x
    while y > 0
      s += y % 10
      y /= 10
    end
    groups[s] << x
  end
  prev_vals = groups[digit_sum[0]]
  dp = Array.new(prev_vals.length, 1)
  (1...digit_sum.length).each do |pos|
    cur_vals = groups[digit_sum[pos]]
    nxt = Array.new(cur_vals.length, 0)
    j = 0
    prefix = 0
    cur_vals.each_with_index do |x, i|
      while j < prev_vals.length && prev_vals[j] <= x
        prefix += dp[j]
        prefix -= mod if prefix >= mod
        j += 1
      end
      nxt[i] = prefix
    end
    prev_vals = cur_vals
    dp = nxt
  end
  ans = 0
  dp.each do |x|
    ans += x
    ans -= mod if ans >= mod
  end
  ans
end
