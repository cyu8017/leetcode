# LeetCode 3104 - Find Longest Self-Contained Substring
# https://leetcode.com/problems/find-longest-self-contained-substring/

# @param {String} s
# @return {Integer}
def max_substring_length(s)
  first = Array.new(26, -1)
  last = Array.new(26, 0)
  n = s.length
  s.each_char.with_index do |ch, i|
    j = ch.ord - 97
    first[j] = i if first[j] == -1
    last[j] = i
  end
  ans = -1
  26.times do |k|
    i = first[k]
    next if i == -1
    mx = last[k]
    (i...n).each do |j|
      a = first[s[j].ord - 97]
      b = last[s[j].ord - 97]
      break if a < i
      mx = [mx, b].max
      ans = [ans, j - i + 1].max if mx == j && j - i + 1 < n
    end
  end
  ans
end
