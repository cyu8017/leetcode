# LeetCode 0773 - Sliding Puzzle
# https://leetcode.com/problems/sliding-puzzle/

# @param {Integer[][]} board
# @return {Integer}
def sliding_puzzle(board)
  start = board.flatten.join
  target = "123450"
  neighbors = {
    0 => [1, 3],
    1 => [0, 2, 4],
    2 => [1, 5],
    3 => [0, 4],
    4 => [1, 3, 5],
    5 => [2, 4]
  }
  queue = [[start, 0]]
  seen = { start => true }
  until queue.empty?
    state, steps = queue.shift
    return steps if state == target

    zero = state.index("0")
    neighbors[zero].each do |nei|
      chars = state.chars
      chars[zero], chars[nei] = chars[nei], chars[zero]
      nxt = chars.join
      next if seen[nxt]

      seen[nxt] = true
      queue << [nxt, steps + 1]
    end
  end
  -1
end
