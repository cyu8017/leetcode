# LeetCode 0076 - Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/

# @param {String} s
# @param {String} t
# @return {String}
def min_window(s, t)
  return "" if t.empty?

  need = Hash.new(0)
  t.each_char { |ch| need[ch] += 1 }

  required = need.length
  formed = 0
  window = Hash.new(0)
  left = 0
  best_len = Float::INFINITY
  best_left = 0

  s.each_char.with_index do |ch, right|
    window[ch] += 1
    formed += 1 if need.key?(ch) && window[ch] == need[ch]

    while formed == required
      if right - left + 1 < best_len
        best_len = right - left + 1
        best_left = left
      end

      left_ch = s[left]
      window[left_ch] -= 1
      formed -= 1 if need.key?(left_ch) && window[left_ch] < need[left_ch]
      left += 1
    end
  end

  return "" if best_len == Float::INFINITY

  s[best_left, best_len]
end
