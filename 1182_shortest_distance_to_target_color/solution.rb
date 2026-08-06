# LeetCode 1182 - Shortest Distance to Target Color
# https://leetcode.com/problems/shortest-distance-to-target-color/

# @param {Integer[]} colors
# @param {Integer[][]} queries
# @return {Integer[]}
def shortest_distance_color(colors, queries)
  pos = Hash.new { |h, k| h[k] = [] }
  colors.each_with_index { |c, i| pos[c] << i }
  queries.map do |i, c|
    next -1 unless pos.key?(c)
    arr = pos[c]
    idx = arr.bsearch_index { |x| x >= i } || arr.length
    best = Float::INFINITY
    best = [best, arr[idx] - i].min if idx < arr.length
    best = [best, i - arr[idx - 1]].min if idx > 0
    best == Float::INFINITY ? -1 : best
  end
end
