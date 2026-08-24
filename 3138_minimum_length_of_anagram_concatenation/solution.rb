# LeetCode 3138 - Minimum Length of Anagram Concatenation
# https://leetcode.com/problems/minimum-length-of-anagram-concatenation/

# @param {String} s
# @return {Integer}
def min_anagram_length(s)
  n = s.length
  cnt = Array.new(26, 0)
  s.each_char { |ch| cnt[ch.ord - 97] += 1 }

  check = lambda do |k|
    (0...n).step(k) do |i|
      cnt1 = Array.new(26, 0)
      (i...i + k).each { |j| cnt1[s[j].ord - 97] += 1 }
      26.times { |j| return false if cnt1[j] * (n / k) != cnt[j] }
    end
    true
  end

  i = 1
  loop do
    return i if n % i == 0 && check.call(i)
    i += 1
  end
end
