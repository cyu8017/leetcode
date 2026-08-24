# LeetCode 0886 - Possible Bipartition
# https://leetcode.com/problems/possible-bipartition/

# @param {Integer} n
# @param {Integer[][]} dislikes
# @return {Boolean}
def possible_bipartition(n, dislikes)
  graph = Hash.new { |h, k| h[k] = [] }
  dislikes.each do |a, b|
    graph[a] << b
    graph[b] << a
  end
  color = {}
  (1..n).each do |start|
    next if color.key?(start)

    queue = [start]
    color[start] = 0
    until queue.empty?
      node = queue.shift
      graph[node].each do |nei|
        if !color.key?(nei)
          color[nei] = color[node] ^ 1
          queue << nei
        elsif color[nei] == color[node]
          return false
        end
      end
    end
  end
  true
end
