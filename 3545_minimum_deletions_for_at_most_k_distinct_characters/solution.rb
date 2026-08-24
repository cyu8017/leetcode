# LeetCode 3545 - Minimum Deletions for At Most K Distinct Characters
# https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def min_deletion(s, k)
  cnt = Array.new(26, 0)
  s.each_char { |c| cnt[c.ord - 97] += 1 }
  cnt.sort!
  ans = 0
  (0...(26 - k)).each { |i| ans += cnt[i] }
  ans
end
