# LeetCode 0399 - Evaluate Division
# https://leetcode.com/problems/evaluate-division/

require "set"

class Solution
  def calc_equation(equations, values, queries)
    graph = Hash.new { |hash, key| hash[key] = {} }

    equations.zip(values).each do |(dividend, divisor), value|
      graph[dividend][divisor] = value
      graph[divisor][dividend] = 1.0 / value
    end

    dfs = lambda do |start, finish, visited|
      return -1.0 unless graph.key?(start) && graph.key?(finish)
      return 1.0 if start == finish

      visited.add(start)
      graph[start].each do |neighbor, weight|
        next if visited.include?(neighbor)

        result = dfs.call(neighbor, finish, visited)
        return weight * result if result != -1.0
      end
      -1.0
    end

    queries.map do |start, finish|
      dfs.call(start, finish, Set.new)
    end
  end

  alias_method :calcEquation, :calc_equation
end
