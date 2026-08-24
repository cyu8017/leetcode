# LeetCode 2044 - Count Number of Maximum Bitwise-OR Subsets
# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

# @param {Integer[]} nums
# @return {Integer}
def count_max_or_subsets(nums)
  max_or = 0
  nums.each { |x| max_or |= x }
  ans = 0
  dfs = lambda do |i, cur|
    if i == nums.length
      ans += 1 if cur == max_or
      return
    end
    dfs.call(i + 1, cur)
    dfs.call(i + 1, cur | nums[i])
  end
  dfs.call(0, 0)
  ans
end
