# LeetCode 1915 - Number of Wonderful Substrings
# https://leetcode.com/problems/number-of-wonderful-substrings/

# @param {String} word
# @return {Integer}
def wonderful_substrings(word)
  count = Array.new(1024, 0)
  count[0] = 1
  mask = 0
  ans = 0
  word.each_char do |ch|
    mask ^= 1 << (ch.ord - 97)
    ans += count[mask]
    10.times { |bit| ans += count[mask ^ (1 << bit)] }
    count[mask] += 1
  end
  ans
end
