# LeetCode 3090 - Maximum Length Substring With Two Occurrences
# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/

# @param {String} s
# @return {Integer}
def maximum_length_substring(s)
  l = 0
  ans = 0
  cnt = Array.new(26, 0)
  s.each_char.with_index do |ch, r|
    idx = ch.ord - 97
    cnt[idx] += 1
    while cnt[idx] > 2
      cnt[s[l].ord - 97] -= 1
      l += 1
    end
    ans = [ans, r - l + 1].max
  end
  ans
end
