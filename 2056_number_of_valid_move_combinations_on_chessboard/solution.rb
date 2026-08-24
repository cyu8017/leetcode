# LeetCode 2056 - Number of Valid Move Combinations On Chessboard
# https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/

# @param {String[]} pieces
# @param {Integer[][]} positions
# @return {Integer}
def count_combinations(pieces, positions)
  dirs = {
    "rook" => [[1, 0], [-1, 0], [0, 1], [0, -1]],
    "bishop" => [[1, 1], [1, -1], [-1, 1], [-1, -1]],
    "queen" => [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
  }
  n = pieces.length
  all_moves = []
  n.times do |i|
    ms = [{ dr: 0, dc: 0, steps: 0 }]
    r, c = positions[i]
    dirs[pieces[i]].each do |dr, dc|
      nr = r + dr
      nc = c + dc
      step = 1
      while nr.between?(1, 8) && nc.between?(1, 8)
        ms << { dr: dr, dc: dc, steps: step }
        nr += dr
        nc += dc
        step += 1
      end
    end
    all_moves << ms
  end
  chosen = Array.new(n)
  ans = 0

  ok_combo = lambda do |last|
    max_t = (0..last).map { |i| chosen[i][:steps] }.max
    (1..max_t).each do |t|
      seen = {}
      (0..last).each do |i|
        m = chosen[i]
        if m[:steps].zero?
          pr, pc = positions[i]
        else
          use = [t, m[:steps]].min
          pr = positions[i][0] + m[:dr] * use
          pc = positions[i][1] + m[:dc] * use
        end
        key = (pr << 32) ^ (pc & 0xFFFFFFFF)
        return false if seen[key]

        seen[key] = true
      end
    end
    true
  end

  dfs = lambda do |i|
    if i == pieces.length
      ans += 1
      return
    end
    all_moves[i].each do |m|
      chosen[i] = m
      dfs.call(i + 1) if ok_combo.call(i)
    end
  end
  dfs.call(0)
  ans
end
