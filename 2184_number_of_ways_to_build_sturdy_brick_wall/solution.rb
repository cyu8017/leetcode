# LeetCode 2184 - Number of Ways to Build Sturdy Brick Wall
# https://leetcode.com/problems/number-of-ways-to-build-sturdy-brick-wall/

# @param {Integer} height
# @param {Integer} width
# @param {Integer[]} bricks
# @return {Integer}
def build_wall(height, width, bricks)
  mod = 1_000_000_007
  masks = []
  gen = nil
  gen = lambda do |remain, mask|
    if remain == 0
      masks << mask
      return
    end
    bricks.each do |b|
      next if b > remain

      nm = mask
      nm |= 1 << (remain - b) if remain - b > 0
      gen.call(remain - b, nm)
    end
  end
  gen.call(width, 0)
  m = masks.length
  compat = Array.new(m) { [] }
  m.times do |i|
    m.times { |j| compat[i] << j if (masks[i] & masks[j]).zero? }
  end
  dp = Array.new(m, 1)
  (1...height).each do
    ndp = Array.new(m, 0)
    m.times do |i|
      compat[i].each { |j| ndp[j] = (ndp[j] + dp[i]) % mod }
    end
    dp = ndp
  end
  dp.sum % mod
end
