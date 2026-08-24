# LeetCode 2522 - Partition String Into Substrings With Values At Most K
# https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def minimum_partition(s, k)
  ans = 1
  cur = 0
  s.each_char do |ch|
    d = ch.ord - 48
    return -1 if d > k

    nxt = cur * 10 + d
    if nxt > k
      ans += 1
      cur = d
    else
      cur = nxt
    end
  end
  ans
end
