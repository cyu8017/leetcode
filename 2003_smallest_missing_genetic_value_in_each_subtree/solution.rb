# LeetCode 2003 - Smallest Missing Genetic Value in Each Subtree
# https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/

# @param {Integer[]} parents
# @param {Integer[]} nums
# @return {Integer[]}
def smallest_missing_value_subtree(parents, nums)
  n = parents.length
  children = Array.new(n) { [] }
  (1...n).each { |i| children[parents[i]] << i }
  ans = Array.new(n, 1)
  one = nums.index(1)
  return ans if one.nil?

  seen = {}
  collect = lambda do |u|
    return if seen[nums[u]]

    seen[nums[u]] = true
    children[u].each { |v| collect.call(v) }
  end
  miss = 1
  node = one
  prev = -1
  while node != -1
    children[node].each { |v| collect.call(v) if v != prev }
    seen[nums[node]] = true
    miss += 1 while seen[miss]
    ans[node] = miss
    prev = node
    node = parents[node]
  end
  ans
end
