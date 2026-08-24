# LeetCode 0675 - Cut Off Trees for Golf Event
# https://leetcode.com/problems/cut-off-trees-for-golf-event/

# @param {Integer[][]} forest
# @return {Integer}
def cut_off_tree(forest)
  m = forest.length
  n = forest[0].length
  trees = []
  m.times do |i|
    n.times do |j|
      trees << [forest[i][j], i, j] if forest[i][j] > 1
    end
  end
  trees.sort!

  bfs = lambda do |sr, sc, tr, tc|
    return 0 if sr == tr && sc == tc

    seen = { [sr, sc] => true }
    queue = [[sr, sc, 0]]
    until queue.empty?
      r, c, dist = queue.shift
      [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]].each do |nr, nc|
        next unless nr >= 0 && nr < m && nc >= 0 && nc < n
        next if seen.key?([nr, nc]) || forest[nr][nc].zero?
        return dist + 1 if nr == tr && nc == tc

        seen[[nr, nc]] = true
        queue << [nr, nc, dist + 1]
      end
    end
    -1
  end

  sr = 0
  sc = 0
  steps = 0
  trees.each do |_, tr, tc|
    dist = bfs.call(sr, sc, tr, tc)
    return -1 if dist < 0

    steps += dist
    sr = tr
    sc = tc
  end
  steps
end
