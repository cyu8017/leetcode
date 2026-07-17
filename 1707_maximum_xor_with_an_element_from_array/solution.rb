# LeetCode 1707 - Maximum XOR With an Element From Array
# https://leetcode.com/problems/maximum-xor-with-an-element-from-array/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def maximize_xor(nums, queries)
  nums = nums.sort
  order = (0...queries.length).sort_by { |i| queries[i][1] }

  children = [[-1, -1]]

  insert = lambda do |num|
    node = 0
    31.downto(0) do |bit|
      b = (num >> bit) & 1
      if children[node][b] == -1
        children[node][b] = children.length
        children << [-1, -1]
      end
      node = children[node][b]
    end
  end

  ans = Array.new(queries.length, -1)
  added = 0
  order.each do |qi|
    x, limit = queries[qi]
    while added < nums.length && nums[added] <= limit
      insert.call(nums[added])
      added += 1
    end
    next if added.zero?
    node = 0
    value = 0
    31.downto(0) do |bit|
      b = (x >> bit) & 1
      want = b ^ 1
      if children[node][want] != -1
        value |= 1 << bit
        node = children[node][want]
      else
        node = children[node][b]
      end
    end
    ans[qi] = value
  end
  ans
end
