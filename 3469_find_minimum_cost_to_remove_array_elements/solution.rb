# LeetCode 3469 - Find Minimum Cost to Remove Array Elements
# https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/

# @param {Integer[]} nums
# @return {Integer}
def min_cost(nums)
  n = nums.length
  memo = {}
  dfs = nil
  dfs = lambda do |i, prev|
    return prev == -1 ? 0 : nums[prev] if i >= n

    k = (i << 32) | (prev & 0xFFFFFFFF)
    return memo[k] if memo.key?(k)

    res = if prev == -1
            if i + 1 >= n
              nums[i]
            elsif i + 2 >= n
              [nums[i], nums[i + 1]].max
            else
              a = nums[i]
              b = nums[i + 1]
              c = nums[i + 2]
              [
                [b, c].max + dfs.call(i + 3, i),
                [a, c].max + dfs.call(i + 3, i + 1),
                [a, b].max + dfs.call(i + 3, i + 2)
              ].min
            end
          elsif i + 1 >= n
            [nums[prev], nums[i]].max
          else
            a = nums[prev]
            b = nums[i]
            c = nums[i + 1]
            [
              [b, c].max + dfs.call(i + 2, prev),
              [a, c].max + dfs.call(i + 2, i),
              [a, b].max + dfs.call(i + 2, i + 1)
            ].min
          end
    memo[k] = res
    res
  end
  dfs.call(0, -1)
end
