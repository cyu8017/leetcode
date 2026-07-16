# LeetCode 0547 - Number of Provinces
# https://leetcode.com/problems/number-of-provinces/

class Solution
  def find_circle_num(is_connected)
    n = is_connected.length
    parent = (0...n).to_a

    find = lambda do |x|
      while parent[x] != x
        parent[x] = parent[parent[x]]
        x = parent[x]
      end
      x
    end

    union = lambda do |a, b|
      ra = find.call(a)
      rb = find.call(b)
      parent[rb] = ra if ra != rb
    end

    (0...n).each do |i|
      ((i + 1)...n).each do |j|
        union.call(i, j) if is_connected[i][j] != 0
      end
    end

    (0...n).count { |i| find.call(i) == i }
  end

  alias_method :findCircleNum, :find_circle_num
end
