# LeetCode 3514 - Number of Unique XOR Triplets II
# https://leetcode.com/problems/number-of-unique-xor-triplets-ii/

# @param {Integer[]} nums
# @return {Integer}
def unique_xor_triplets(nums)
  mx = 0
  nums.each { |v| mx = [mx, v].max }
  mx <<= 1
  st = Array.new(mx, false)
  nums.each do |a|
    nums.each { |b| st[a ^ b] = true }
  end
  s = Array.new(mx, 0)
  (0...mx).each do |ab|
    next unless st[ab]
    nums.each { |c| s[ab ^ c] = 1 }
  end
  ans = 0
  s.each { |v| ans += v }
  ans
end
