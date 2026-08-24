# LeetCode 3444 - Minimum Increments for Target Multiples in an Array
# https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/

# @param {Integer[]} nums
# @param {Integer[]} target
# @return {Integer}
def minimum_increments(nums, target)
  m = target.length
  nmask = 1 << m
  inf = 10**18
  dp = Array.new(nmask, inf)
  dp[0] = 0
  nums.each do |x|
    ndp = dp.dup
    (0...nmask).each do |mask|
      (1...nmask).each do |sub|
        l = 1
        ok = true
        (0...m).each do |i|
          next if (sub & (1 << i)) == 0

          l = lcm_3444(l, target[i])
          if l > 1_000_000_000
            ok = false
            break
          end
        end
        next unless ok

        cost = (l - x % l) % l
        nm = mask | sub
        ndp[nm] = dp[mask] + cost if dp[mask] + cost < ndp[nm]
      end
    end
    dp = ndp
  end
  dp[nmask - 1]
end

def gcd_3444(a, b)
  while b != 0
    a, b = b, a % b
  end
  a
end

def lcm_3444(a, b)
  a / gcd_3444(a, b) * b
end
