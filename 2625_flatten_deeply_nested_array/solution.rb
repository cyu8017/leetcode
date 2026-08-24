# LeetCode 2625 - Flatten Deeply Nested Array
# https://leetcode.com/problems/flatten-deeply-nested-array/

# @param {Object[]} arr
# @param {Integer} n
# @return {Object[]}
def flat(arr, n)
  res = []
  dfs = lambda do |a, depth|
    a.each do |x|
      if x.is_a?(Array) && depth < n
        dfs.call(x, depth + 1)
      else
        res << x
      end
    end
  end
  dfs.call(arr, 0)
  res
end
