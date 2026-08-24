# LeetCode 3670 - Maximum Product of Two Integers With No Common Bits
# https://leetcode.com/problems/maximum-product-of-two-integers-with-no-common-bits/

# @param {Integer[]} nums
# @return {Integer}
def max_product(nums)
  max_v = nums.empty? ? 0 : nums.max
  bits_n = 0
  x = max_v
  while x > 0
    bits_n += 1
    x >>= 1
  end
  bits_n = 1 if bits_n == 0
  size = 1 << bits_n
  best = Array.new(size, 0)
  nums.each { |v| best[v] = v if v > best[v] }
  (0...size).each do |mask|
    (0...bits_n).each do |b|
      next if (mask & (1 << b)) == 0

      sub = mask ^ (1 << b)
      best[mask] = best[sub] if best[sub] > best[mask]
    end
  end
  ans = 0
  nums.each do |v|
    comp = (size - 1) ^ v
    if best[comp] > 0
      p = v * best[comp]
      ans = p if p > ans
    end
  end
  ans
end
