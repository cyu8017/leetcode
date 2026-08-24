# LeetCode 0647 - Palindromic Substrings
# https://leetcode.com/problems/palindromic-substrings/

# @param {String} s
# @return {Integer}
def count_substrings(s)
  expand = lambda do |left, right|
    count = 0
    while left >= 0 && right < s.length && s[left] == s[right]
      count += 1
      left -= 1
      right += 1
    end
    count
  end

  total = 0
  s.length.times do |i|
    total += expand.call(i, i)
    total += expand.call(i, i + 1)
  end
  total
end
