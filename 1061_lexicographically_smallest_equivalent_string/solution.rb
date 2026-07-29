# LeetCode 1061 - Lexicographically Smallest Equivalent String
# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

# @param {String} s1
# @param {String} s2
# @param {String} base_str
# @return {String}
def smallest_equivalent_string(s1, s2, base_str)
  parent = (0...26).to_a

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
    return if ra == rb

    if ra < rb
      parent[rb] = ra
    else
      parent[ra] = rb
    end
  end

  s1.chars.zip(s2.chars).each do |a, b|
    union.call(a.ord - 97, b.ord - 97)
  end
  base_str.chars.map { |c| (find.call(c.ord - 97) + 97).chr }.join
end
