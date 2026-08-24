# LeetCode 2440 - Create Components With Same Value
# https://leetcode.com/problems/create-components-with-same-value/

# @param {Integer[]} nums
# @param {Integer[][]} edges
# @return {Integer}
def component_value(nums, edges)
  n = nums.length
  total = nums.sum
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end

  dfs = lambda do |u, p, target|
    s = nums[u]
    g[u].each do |v|
      next if v == p

      sub = dfs.call(v, u, target)
      return -1 if sub < 0

      s += sub
    end
    return -1 if s > target
    return 0 if s == target

    s
  end

  n.downto(1) do |parts|
    next if total % parts != 0

    return parts - 1 if dfs.call(0, -1, total / parts) == 0
  end
  0
end
