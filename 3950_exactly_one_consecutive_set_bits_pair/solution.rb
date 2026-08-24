# LeetCode 3950 - Exactly One Consecutive Set Bits Pair
# https://leetcode.com/problems/exactly-one-consecutive-set-bits-pair/

# @param {Integer} n
# @return {Boolean}
def consecutive_set_bits(n)
  vis = false
  pre = 0
  while n > 0
    cur = n & 1
    if pre == cur && cur == 1
      return false if vis
      vis = true
    end
    pre = cur
    n >>= 1
  end
  vis
end
