# LeetCode 1177 - Can Make Palindrome from Substring
# https://leetcode.com/problems/can-make-palindrome-from-substring/

# @param {String} s
# @param {Integer[][]} queries
# @return {Boolean[]}
def can_make_pali_queries(s, queries)
  prefix = [0]
  mask = 0
  s.each_char do |ch|
    mask ^= 1 << (ch.ord - 97)
    prefix << mask
  end
  queries.map do |left, right, k|
    bits = (prefix[right + 1] ^ prefix[left]).to_s(2).count("1")
    bits / 2 <= k
  end
end
