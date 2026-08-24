# LeetCode 0899 - Orderly Queue
# https://leetcode.com/problems/orderly-queue/

# @param {String} s
# @param {Integer} k
# @return {String}
def orderly_queue(s, k)
  return s.chars.sort.join if k > 1

  (0...s.length).map { |i| s[i..] + s[0...i] }.min
end
