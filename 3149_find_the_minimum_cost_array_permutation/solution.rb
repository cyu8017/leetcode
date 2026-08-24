# LeetCode 3149 - Find the Minimum Cost Array Permutation
# https://leetcode.com/problems/find-the-minimum-cost-array-permutation/

# @param {Integer[]} nums
# @return {Integer[]}
def find_permutation(nums)
  n = nums.length
  memo = Array.new(1 << n) { Array.new(n, -1) }

  absv = ->(x) { x < 0 ? -x : x }

  dfs = nil
  dfs = lambda do |mask, pre|
    return absv.call(pre - nums[0]) if mask == (1 << n) - 1
    return memo[mask][pre] if memo[mask][pre] != -1
    res = 10**18
    (1...n).each do |cur|
      if ((mask >> cur) & 1) == 0
        res = [res, absv.call(pre - nums[cur]) + dfs.call(mask | (1 << cur), cur)].min
      end
    end
    memo[mask][pre] = res
    res
  end

  ans = []
  g = nil
  g = lambda do |mask, pre|
    ans << pre
    return if mask == (1 << n) - 1
    res = dfs.call(mask, pre)
    (1...n).each do |cur|
      if ((mask >> cur) & 1) == 0
        if absv.call(pre - nums[cur]) + dfs.call(mask | (1 << cur), cur) == res
          g.call(mask | (1 << cur), cur)
          break
        end
      end
    end
  end

  g.call(1, 0)
  ans
end
