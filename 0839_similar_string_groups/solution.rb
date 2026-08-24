# LeetCode 0839 - Similar String Groups
# https://leetcode.com/problems/similar-string-groups/

# @param {String[]} strs
# @return {Integer}
def num_similar_groups(strs)
  n = strs.length
  parent = (0...n).to_a

  find = lambda do |x|
    while parent[x] != x
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end

  similar = lambda do |a, b|
    diff = []
    a.length.times { |i| diff << i if a[i] != b[i] }
    diff.empty? || (diff.length == 2 && a[diff[0]] == b[diff[1]] && a[diff[1]] == b[diff[0]])
  end

  groups = n
  n.times do |i|
    ((i + 1)...n).each do |j|
      next unless similar.call(strs[i], strs[j])

      pi = find.call(i)
      pj = find.call(j)
      if pi != pj
        parent[pi] = pj
        groups -= 1
      end
    end
  end
  groups
end
