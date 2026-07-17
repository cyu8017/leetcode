# LeetCode 1787 - Make the XOR of All Segments Equal to Zero
# https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_changes(nums, k)
  freq = Array.new(k) { Hash.new(0) }
  size = Array.new(k, 0)
  nums.each_with_index do |x, i|
    freq[i % k][x] += 1
    size[i % k] += 1
  end
  inf = 10**9
  dp = { 0 => 0 }
  k.times do |i|
    ndp = {}
    256.times do |xv|
      cost = size[i] - freq[i][xv]
      dp.each do |xo, changes|
        key = xo ^ xv
        value = changes + cost
        ndp[key] = value if ndp.fetch(key, inf) > value
      end
    end
    dp = ndp
  end
  dp[0]
end
