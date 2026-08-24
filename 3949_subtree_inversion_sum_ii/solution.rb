# LeetCode 3949 - Subtree Inversion Sum II
# https://leetcode.com/problems/subtree-inversion-sum-ii/

# @param {Integer[][]} edges
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_subtree_inversion_sum(edges, nums, k)
  n = nums.length
  graph = Array.new(n) { [] }
  edges.each do |edge|
    graph[edge[0]] << edge[1]
    graph[edge[1]] << edge[0]
  end
  parent = Array.new(n, -2)
  parent[0] = -1
  order = [0]
  i = 0
  while i < order.length
    u = order[i]
    graph[u].each do |v|
      if parent[v] == -2
        parent[v] = u
        order << v
      end
    end
    i += 1
  end
  infinity = 2**60
  maximum = Array.new(n)
  minimum = Array.new(n)
  (n - 1).downto(0) do |oi|
    u = order[oi]
    current_max = Array.new(k + 1, -infinity)
    current_min = Array.new(k + 1, infinity)
    current_max[k] = current_min[k] = nums[u]
    graph[u].each do |v|
      next if parent[v] != u
      next_max = Array.new(k + 1, -infinity)
      next_min = Array.new(k + 1, infinity)
      (0..k).each do |first|
        next if current_max[first] == -infinity
        (0..k).each do |child_distance|
          next if maximum[v][child_distance] == -infinity
          second = child_distance + 1
          second = k if second > k
          next if first < k && second < k && first + second < k
          distance = [first, second].min
          max_value = current_max[first] + maximum[v][child_distance]
          min_value = current_min[first] + minimum[v][child_distance]
          next_max[distance] = max_value if max_value > next_max[distance]
          next_min[distance] = min_value if min_value < next_min[distance]
        end
      end
      current_max = next_max
      current_min = next_min
    end
    current_max[0] = -current_min[k] if -current_min[k] > current_max[0]
    current_min[0] = -current_max[k] if -current_max[k] < current_min[0]
    maximum[u] = current_max
    minimum[u] = current_min
  end
  answer = -(2**60)
  maximum[0].each { |value| answer = value if value > answer }
  answer
end
