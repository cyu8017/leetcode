# LeetCode 3966 - Count Good Integers in a Range
# https://leetcode.com/problems/count-good-integers-in-a-range/

# @param {Integer} l
# @param {Integer} r
# @param {Integer} k
# @return {Integer}
def count_good_integers(l, r, k)
  dfs = nil
  dfs = lambda do |position, previous, started, tight, digits, k, memo|
    return started ? 1 : 0 if position == digits.length
    key = [position, previous, started]
    return memo[key] if !tight && memo.key?(key)
    limit = tight ? digits[position].ord - 48 : 9
    result = 0
    (0..limit).each do |digit|
      next_started = started || digit != 0
      next if started && (previous - digit).abs > k
      next_previous = next_started ? digit : previous
      result += dfs.call(position + 1, next_previous, next_started, tight && digit == limit, digits, k, memo)
    end
    memo[key] = result unless tight
    result
  end
  count = lambda do |bound, k|
    return 0 if bound <= 0
    digits = bound.to_s
    dfs.call(0, 0, false, true, digits, k, {})
  end
  count.call(r, k) - count.call(l - 1, k)
end
