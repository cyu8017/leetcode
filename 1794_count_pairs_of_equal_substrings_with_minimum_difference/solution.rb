# LeetCode 1794 - Count Pairs of Equal Substrings With Minimum Difference
# https://leetcode.com/problems/count-pairs-of-equal-substrings-with-minimum-difference/

# @param {String} first_string
# @param {String} second_string
# @return {Integer}
def count_quadruples(first_string, second_string)
  first = {}
  last_f = {}
  last_s = {}
  first_string.each_char.with_index do |ch, i|
    first[ch] = i unless first.key?(ch)
    last_f[ch] = i
  end
  second_string.each_char.with_index do |ch, i|
    last_s[ch] = i
  end
  best = Float::INFINITY
  first.each_key do |ch|
    best = [best, last_f[ch] - last_s[ch]].min if last_s.key?(ch)
  end
  return 0 if best == Float::INFINITY
  ans = 0
  first.each_key do |ch|
    next if !last_s.key?(ch) || last_f[ch] - last_s[ch] != best
    i_count = (first[ch]..last_f[ch]).count { |k| first_string[k] == ch }
    a_count = (0..last_s[ch]).count { |k| second_string[k] == ch }
    ans += i_count * a_count
  end
  ans
end
