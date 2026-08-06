# LeetCode 1496 - Path Crossing
# https://leetcode.com/problems/path-crossing/

def is_path_crossing(path)
  x = y = 0
  seen = { [0, 0] => true }
  move = { 'N' => [0, 1], 'S' => [0, -1], 'E' => [1, 0], 'W' => [-1, 0] }
  path.each_char do |c|
    dx, dy = move[c]
    x += dx
    y += dy
    return true if seen[[x, y]]
    seen[[x, y]] = true
  end
  false
end
