# LeetCode 1059 - All Paths from Source Lead to Destination
# https://leetcode.com/problems/all-paths-from-source-lead-to-destination/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} source
# @param {Integer} destination
# @return {Boolean}
def leads_to_destination(n, edges, source, destination)
  graph = Array.new(n) { [] }
  edges.each { |a, b| graph[a] << b }
  state = Array.new(n, 0)

  dfs = lambda do |node|
    return node == destination if graph[node].empty?
    return false if state[node] == 1
    return true if state[node] == 2

    state[node] = 1
    graph[node].each do |nxt|
      return false unless dfs.call(nxt)
    end
    state[node] = 2
    true
  end

  dfs.call(source)
end
