# LeetCode 0990 - Satisfiability of Equality Equations
# https://leetcode.com/problems/satisfiability-of-equality-equations/

# @param {String[]} equations
# @return {Boolean}
def equations_possible(equations)
  parent = (0...26).to_a
  find = lambda do |x|
    while parent[x] != x
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end
  equations.each do |eq|
    parent[find.call(eq[0].ord - 97)] = find.call(eq[3].ord - 97) if eq[1] == "="
  end
  equations.each do |eq|
    return false if eq[1] == "!" && find.call(eq[0].ord - 97) == find.call(eq[3].ord - 97)
  end
  true
end
