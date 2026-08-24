# LeetCode 0696 - Count Binary Substrings
# https://leetcode.com/problems/count-binary-substrings/

# @param {String} s
# @return {Integer}
def count_binary_substrings(s)
  prev = 0
  cur = 1
  ans = 0
  (1...s.length).each do |i|
    if s[i] == s[i - 1]
      cur += 1
    else
      ans += [prev, cur].min
      prev = cur
      cur = 1
    end
  end
  ans + [prev, cur].min
end
