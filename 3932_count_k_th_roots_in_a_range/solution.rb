# LeetCode 3932 - Count K Th Roots In A Range
# https://leetcode.com/problems/count-k-th-roots-in-a-range/

# @param {Integer} l
# @param {Integer} r
# @param {Integer} k
# @return {Integer}
def count_kth_roots(l, r, k)
  return r - l + 1 if k == 1
  ans = 0
  x = 0
  loop do
    y = 1
    too_big = false
    k.times do
      if x != 0 && y > r / x
        too_big = true
        break
      end
      y *= x
      break if y > r
    end
    break if too_big || y > r
    ans += 1 if l <= y && y <= r
    x += 1
  end
  ans
end
