# LeetCode 2741 - Special Permutations
# https://leetcode.com/problems/special-permutations/

# @param {Integer[]} nums
# @return {Integer}
def special_perm(nums)
  mod = 1_000_000_007
  n = nums.length
  memo = Array.new(1 << n) { Array.new(n, -1) }

  dfs = lambda do |mask, last|
    return 1 if mask == (1 << n) - 1
    return memo[mask][last] if memo[mask][last] != -1
    res = 0
    (0...n).each do |i|
      next if (mask & (1 << i)) != 0
      if nums[i] % nums[last] == 0 || nums[last] % nums[i] == 0
        res = (res + dfs.call(mask | (1 << i), i)) % mod
      end
    end
    memo[mask][last] = res
    res
  end

  ans = 0
  (0...n).each { |i| ans = (ans + dfs.call(1 << i, i)) % mod }
  ans
end
