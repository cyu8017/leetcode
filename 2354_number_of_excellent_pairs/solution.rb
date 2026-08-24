# LeetCode 2354 - Number of Excellent Pairs
# https://leetcode.com/problems/number-of-excellent-pairs/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_excellent_pairs(nums, k)
  uniq = {}
  nums.each { |x| uniq[x] = true }
  cnt = Array.new(32, 0)
  bit_count = lambda do |x|
    c = 0
    while x != 0
      x &= x - 1
      c += 1
    end
    c
  end
  uniq.each_key { |x| cnt[bit_count.call(x)] += 1 }
  ans = 0
  (0...32).each do |i|
    (0...32).each { |j| ans += cnt[i] * cnt[j] if i + j >= k }
  end
  ans
end
