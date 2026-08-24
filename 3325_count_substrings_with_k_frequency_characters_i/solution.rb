# LeetCode 3325 - Count Substrings With K-Frequency Characters I
# https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def number_of_substrings(s, k)
  n = s.length
  ans = 0
  n.times do |i|
    freq = Array.new(26, 0)
    (i...n).each do |j|
      freq[s[j].ord - 97] += 1
      if freq.any? { |f| f >= k }
        ans += n - j
        break
      end
    end
  end
  ans
end
