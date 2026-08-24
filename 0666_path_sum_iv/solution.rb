# LeetCode 0666 - Path Sum IV
# https://leetcode.com/problems/path-sum-iv/

# @param {Integer[]} nums
# @return {Integer}
def path_sum(nums)
  tree = {}
  nums.each do |num|
    depth = num / 100
    pos = (num / 10) % 10
    val = num % 10
    tree[[depth, pos]] = val
  end

  total = 0
  dfs = lambda do |depth, pos, path|
    return unless tree.key?([depth, pos])

    path += tree[[depth, pos]]
    left = [depth + 1, pos * 2 - 1]
    right = [depth + 1, pos * 2]
    if !tree.key?(left) && !tree.key?(right)
      total += path
      return
    end
    dfs.call(depth + 1, pos * 2 - 1, path)
    dfs.call(depth + 1, pos * 2, path)
  end

  dfs.call(1, 1, 0)
  total
end
