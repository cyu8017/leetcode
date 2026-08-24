# LeetCode 2582 - Pass the Pillow
# https://leetcode.com/problems/pass-the-pillow/

# @param {Integer} n
# @param {Integer} time
# @return {Integer}
def pass_the_pillow(n, time)
  cycle = 2 * (n - 1)
  t = time % cycle
  return 1 + t if t < n

  n - (t - (n - 1))
end
