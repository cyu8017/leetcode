# LeetCode 3547 - Maximum Sum of Edge Values in a Graph
# https://leetcode.com/problems/maximum-sum-of-edge-values-in-a-graph/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def max_score(n, edges)
  calc = lambda do |left, right, is_cycle|
    w0 = right
    w1 = right
    score = 0
    (right - 1).downto(left) do |value|
      score += w0 * value
      w0 = w1
      w1 = value
    end
    score += w0 * w1 if is_cycle
    score
  end
  get_comp = lambda do |start, graph, seen|
    comp = [start]
    seen[start] = true
    i = 0
    while i < comp.length
      graph[comp[i]].each do |v|
        unless seen[v]
          seen[v] = true
          comp << v
        end
      end
      i += 1
    end
    comp
  end
  graph = Array.new(n) { [] }
  edges.each do |e|
    graph[e[0]] << e[1]
    graph[e[1]] << e[0]
  end
  seen = Array.new(n, false)
  cycle_sizes = []
  path_sizes = []
  (0...n).each do |i|
    next if seen[i]
    comp = get_comp.call(i, graph, seen)
    all_deg2 = comp.all? { |u| graph[u].length == 2 }
    if all_deg2
      cycle_sizes << comp.length
    elsif comp.length > 1
      path_sizes << comp.length
    end
  end
  ans = 0
  cur_n = n
  cycle_sizes.each do |cs|
    ans += calc.call(cur_n - cs + 1, cur_n, true)
    cur_n -= cs
  end
  path_sizes.sort!.reverse!
  path_sizes.each do |ps|
    ans += calc.call(cur_n - ps + 1, cur_n, false)
    cur_n -= ps
  end
  ans
end
