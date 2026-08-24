# LeetCode 2729 - Check if The Number is Fascinating
# https://leetcode.com/problems/check-if-the-number-is-fascinating/

# @param {Integer} n
# @return {Boolean}
def is_fascinating(n)
  s = n.to_s + (2 * n).to_s + (3 * n).to_s
  return false if s.length != 9
  cnt = Array.new(10, 0)
  s.each_char { |c| cnt[c.ord - 48] += 1 }
  return false if cnt[0] != 0
  (1...10).each { |i| return false if cnt[i] != 1 }
  true
end
