# LeetCode 0803 - Bricks Falling When Hit
# https://leetcode.com/problems/bricks-falling-when-hit/

# @param {Integer[][]} grid
# @param {Integer[][]} hits
# @return {Integer[]}
def hit_bricks(grid, hits)
  m = grid.length
  n = grid[0].length
  roof = m * n
  parent = (0..roof).to_a
  size = Array.new(roof + 1, 1)

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

    parent[ra] = rb
    size[rb] += size[ra]
  end

  idx = ->(r, c) { r * n + c }

  neighbors = lambda do |r, c|
    [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]].select do |nr, nc|
      nr >= 0 && nr < m && nc >= 0 && nc < n
    end
  end

  status = grid.map(&:dup)
  hits.each { |r, c| status[r][c] = 0 }

  m.times do |r|
    n.times do |c|
      next if status[r][c] == 0

      union.call(idx.call(r, c), roof) if r == 0
      neighbors.call(r, c).each do |nr, nc|
        union.call(idx.call(r, c), idx.call(nr, nc)) if status[nr][nc] == 1
      end
    end
  end

  answer = Array.new(hits.length, 0)
  (hits.length - 1).downto(0) do |i|
    r, c = hits[i]
    next if grid[r][c] == 0

    prev = size[find.call(roof)]
    status[r][c] = 1
    union.call(idx.call(r, c), roof) if r == 0
    neighbors.call(r, c).each do |nr, nc|
      union.call(idx.call(r, c), idx.call(nr, nc)) if status[nr][nc] == 1
    end
    curr = size[find.call(roof)]
    answer[i] = [0, curr - prev - 1].max
  end
  answer
end
