# LeetCode 1655 - Distribute Repeating Integers
# https://leetcode.com/problems/distribute-repeating-integers/

# @param {Integer[]} nums
# @param {Integer[]} quantity
# @return {Boolean}
def can_distribute(nums, quantity)
  freq = Hash.new(0)
  nums.each { |x| freq[x] += 1 }
  cnt = freq.values
  quantity = quantity.sort.reverse
  m = quantity.length
  sums = Array.new(1 << m, 0)
  (1...(1 << m)).each do |mask|
    bit = mask & -mask
    sums[mask] = sums[mask ^ bit] + quantity[Math.log2(bit).to_i]
  end
  dp = { 0 => true }
  cnt.each do |c|
    nxt = dp.dup
    dp.each_key do |mask|
      left = ((1 << m) - 1) ^ mask
      sub = left
      while sub.positive?
        nxt[mask | sub] = true if sums[sub] <= c
        sub = (sub - 1) & left
      end
    end
    dp = nxt
  end
  dp.key?((1 << m) - 1)
end
