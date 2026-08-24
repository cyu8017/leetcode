# LeetCode 3533 - Concatenated Divisibility
# https://leetcode.com/problems/concatenated-divisibility/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def concatenated_divisibility(nums, k)
  nums = nums.sort
  n = nums.length
  pows = Array.new(n, 0)
  (0...n).each do |i|
    p = 1
    num = nums[i]
    if num == 0
      p = 10 % k
    else
      x = num
      while x > 0
        p = p * 10 % k
        x /= 10
      end
    end
    pows[i] = p
  end
  memo = {}
  dp = nil
  dp = lambda do |mask, mod|
    return mod == 0 if mask == (1 << n) - 1
    key = (mask << 32) | mod
    return memo[key] if memo.key?(key)
    (0...n).each do |i|
      next unless ((mask >> i) & 1) == 0
      nm = (mod * pows[i] + nums[i]) % k
      if dp.call(mask | (1 << i), nm)
        memo[key] = true
        return true
      end
    end
    memo[key] = false
    false
  end
  reconstruct = nil
  reconstruct = lambda do |mask, mod|
    (0...n).each do |i|
      next unless ((mask >> i) & 1) == 0
      nm = (mod * pows[i] + nums[i]) % k
      if dp.call(mask | (1 << i), nm)
        rest = reconstruct.call(mask | (1 << i), nm)
        rest.unshift(nums[i])
        return rest
      end
    end
    []
  end
  return [] unless dp.call(0, 0)
  reconstruct.call(0, 0)
end
