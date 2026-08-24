# LeetCode 3014 - Minimum Number of Pushes to Type Word I
# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

# @param {String} word
# @return {Integer}
def minimum_pushes(word)
  n = word.length
  ans = 0
  k = 1
  (n / 8).times do
    ans += k * 8
    k += 1
  end
  ans + k * (n % 8)
end
