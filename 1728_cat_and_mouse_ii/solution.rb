# LeetCode 1728 - Cat and Mouse II
# https://leetcode.com/problems/cat-and-mouse-ii/

# @param {String[]} grid
# @param {Integer} cat_jump
# @param {Integer} mouse_jump
# @return {Boolean}
def can_mouse_win(grid, cat_jump, mouse_jump)
  rows = grid.length
  cols = grid[0].length
  total_open = 0
  mouse = cat = food = 0
  (0...rows).each do |r|
    (0...cols).each do |c|
      cell = grid[r][c]
      total_open += 1 if cell != '#'
      case cell
      when 'M' then mouse = r * cols + c
      when 'C' then cat = r * cols + c
      when 'F' then food = r * cols + c
      end
    end
  end
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  compute_moves = lambda do |pos, jump|
    r, c = pos.divmod(cols)
    out = [pos]
    dirs.each do |dr, dc|
      (1..jump).each do |step|
        nr = r + dr * step
        nc = c + dc * step
        break if nr < 0 || nr >= rows || nc < 0 || nc >= cols || grid[nr][nc] == '#'
        out << nr * cols + nc
      end
    end
    out
  end
  cells = rows * cols
  mouse_moves = Array.new(cells)
  cat_moves = Array.new(cells)
  (0...rows).each do |r|
    (0...cols).each do |c|
      next if grid[r][c] == '#'
      pos = r * cols + c
      mouse_moves[pos] = compute_moves.call(pos, mouse_jump)
      cat_moves[pos] = compute_moves.call(pos, cat_jump)
    end
  end
  max_turn = 2 * total_open
  memo = {}
  win = lambda do |m, c, turn|
    return false if turn >= max_turn
    return true if m == food
    return false if c == food || c == m
    key = (m * cells + c) * max_turn + turn
    cached = memo[key]
    return cached unless cached.nil?
    result =
      if turn.even?
        mouse_moves[m].any? { |nm| win.call(nm, c, turn + 1) }
      else
        cat_moves[c].all? { |nc| win.call(m, nc, turn + 1) }
      end
    memo[key] = result
    result
  end
  win.call(mouse, cat, 0)
end
