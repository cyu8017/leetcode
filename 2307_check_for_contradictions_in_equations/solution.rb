# LeetCode 2307 - Check for Contradictions in Equations
# https://leetcode.com/problems/check-for-contradictions-in-equations/

# @param {String[][]} equations
# @param {Float[]} values
# @return {Boolean}
def check_contradictions(equations, values)
  parent = {}
  weight = {}
  find = lambda do |x|
    unless parent.key?(x)
      parent[x] = x
      weight[x] = 1.0
      return x
    end
    if parent[x] != x
      old = parent[x]
      p = find.call(old)
      weight[x] = weight[x] * weight[old]
      parent[x] = p
    end
    parent[x]
  end
  equations.each_with_index do |(a, b), i|
    ra = find.call(a)
    rb = find.call(b)
    if ra == rb
      return true if (weight[a] / weight[b] - values[i]).abs > 1e-5
    else
      parent[ra] = rb
      weight[ra] = values[i] * weight[b] / weight[a]
    end
  end
  false
end

alias solve check_contradictions
