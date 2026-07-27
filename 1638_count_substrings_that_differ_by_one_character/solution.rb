# LeetCode 1638 - Count Substrings That Differ by One Character
# https://leetcode.com/problems/count-substrings-that-differ-by-one-character/

# @param {String} s
# @param {String} t
# @return {Integer}
def count_substrings(s, t)
  ans = 0
  (0...s.length).each do |i|
    (0...t.length).each do |j|
      diff = 0
      [s.length - i, t.length - j].min.times do |k|
        diff += 1 if s[i + k] != t[j + k]
        if diff == 1
          ans += 1
        elsif diff > 1
          break
        end
      end
    end
  end
  ans
end
