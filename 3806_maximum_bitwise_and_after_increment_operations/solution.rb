# LeetCode 3806 - Maximum Bitwise AND After Increment Operations
# https://leetcode.com/problems/maximum-bitwise-and-after-increment-operations/

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} m
# @return {Integer}
def maximum_and(nums, k, m)
  bit_len = lambda do |x|
    return 0 if x == 0
    n = 0
    while x > 0
      n += 1
      x >>= 1
    end
    n
  end
  mx_val = nums[0]
  nums.each { |v| mx_val = v if v > mx_val }
  mx_val += k
  mx = bit_len.call(mx_val)
  ans = 0
  cost = Array.new(nums.length, 0)
  (mx - 1).downto(0) do |bit|
    target = ans | (1 << bit)
    nums.each_with_index do |x, i|
      j = bit_len.call(target & ~x)
      mask = (1 << j) - 1
      cost[i] = (target & mask) - (x & mask)
    end
    cost.sort!
    total = 0
    (0...m).each { |i| total += cost[i] }
    ans = target if total <= k
  end
  ans
end
