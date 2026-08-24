# LeetCode 2127 - Maximum Employees to Be Invited to a Meeting
# https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/

# @param {Integer[]} favorite
# @return {Integer}
def maximum_invitations(favorite)
  n = favorite.length
  indeg = Array.new(n, 0)
  depth = Array.new(n, 1)
  favorite.each { |f| indeg[f] += 1 }
  q = []
  n.times { |i| q << i if indeg[i] == 0 }
  until q.empty?
    u = q.shift
    v = favorite[u]
    depth[v] = [depth[v], depth[u] + 1].max
    indeg[v] -= 1
    q << v if indeg[v] == 0
  end
  pair_sum = 0
  max_cycle = 0
  vis = Array.new(n, false)
  n.times do |i|
    next if indeg[i] == 0 || vis[i]

    u = i
    len_cycle = 0
    until vis[u]
      vis[u] = true
      u = favorite[u]
      len_cycle += 1
    end
    if len_cycle == 2
      pair_sum += depth[i] + depth[favorite[i]]
    else
      max_cycle = [max_cycle, len_cycle].max
    end
  end
  [pair_sum, max_cycle].max
end
