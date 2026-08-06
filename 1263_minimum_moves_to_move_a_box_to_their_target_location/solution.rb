# LeetCode 1263 - Minimum Moves to Move a Box to Their Target Location
# https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/

require "set"

# @param {Character[][]} grid
# @return {Integer}
def min_push_box(grid)
  m = grid.length
  n = grid[0].length
  box = player = target = nil
  m.times do |r|
    n.times do |c|
      case grid[r][c]
      when "B" then box = [r, c]
      when "S" then player = [r, c]
      when "T" then target = [r, c]
      end
    end
  end
  reachable = lambda do |start, blocked|
    seen = Set[start]
    stack = [start]
    until stack.empty?
      r, c = stack.pop
      [[1, 0], [-1, 0], [0, 1], [0, -1]].each do |dr, dc|
        nxt = [r + dr, c + dc]
        next unless nxt[0].between?(0, m - 1) && nxt[1].between?(0, n - 1)
        next if grid[nxt[0]][nxt[1]] == "#" || nxt == blocked || seen.include?(nxt)
        seen.add(nxt)
        stack << nxt
      end
    end
    seen
  end
  queue = [[box, player, 0]]
  seen = Set[[box, player]]
  until queue.empty?
    b, p, pushes = queue.shift
    return pushes if b == target
    can_reach = reachable.call(p, b)
    [[1, 0], [-1, 0], [0, 1], [0, -1]].each do |dr, dc|
      stand = [b[0] - dr, b[1] - dc]
      nb = [b[0] + dr, b[1] + dc]
      next unless can_reach.include?(stand)
      next unless nb[0].between?(0, m - 1) && nb[1].between?(0, n - 1) && grid[nb[0]][nb[1]] != "#"
      state = [nb, b]
      next if seen.include?(state)
      seen.add(state)
      queue << [nb, b, pushes + 1]
    end
  end
  -1
end
