# LeetCode 0797 - All Paths From Source to Target
# https://leetcode.com/problems/all-paths-from-source-to-target/

# @param {Integer[][]} graph
# @return {Integer[][]}
def all_paths_source_target(graph)
  target = graph.length - 1
  answer = []

  dfs = lambda do |node, path|
    if node == target
      answer << path.dup
      return
    end
    graph[node].each do |nei|
      path << nei
      dfs.call(nei, path)
      path.pop
    end
  end

  dfs.call(0, [0])
  answer
end
