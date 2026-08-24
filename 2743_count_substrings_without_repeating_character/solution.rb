# LeetCode 2743 - Count Substrings Without Repeating Character
# https://leetcode.com/problems/count-substrings-without-repeating-character/

# @param {String} s
# @return {Integer}
def number_of_special_substrings(s)
  n = s.length
  ans = 0
  left = 0
  cnt = Array.new(26, 0)
  (0...n).each do |i|
    c = s[i].ord - 97
    cnt[c] += 1
    while cnt[c] > 1
      cnt[s[left].ord - 97] -= 1
      left += 1
    end
    ans += i - left + 1
  end
  ans
end
