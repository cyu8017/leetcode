# LeetCode 3630 - Partition Array for Maximum XOR and AND
# https://leetcode.com/problems/partition-array-for-maximum-xor-and-and/

# @param {Integer[]} nums
# @return {Integer}
def maximize_xor_and_xor(nums)
  n = nums.length
  best = 0
  (0...(1 << n)).each do |mask|
    and_val = -1
    xor_rest = 0
    (0...n).each do |i|
      if ((mask >> i) & 1) != 0
        and_val = and_val < 0 ? nums[i] : (and_val & nums[i])
      else
        xor_rest ^= nums[i]
      end
    end
    and_val = 0 if and_val < 0
    comp = ((1 << n) - 1) ^ mask
    sub = comp
    loop do
      x1 = 0
      (0...n).each { |i| x1 ^= nums[i] if ((sub >> i) & 1) != 0 }
      x2 = xor_rest ^ x1
      v = and_val + x1 + x2
      best = v if v > best
      break if sub == 0

      sub = (sub - 1) & comp
    end
  end
  best
end
