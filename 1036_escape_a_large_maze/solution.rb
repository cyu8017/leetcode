# LeetCode 1036 - Escape a Large Maze
# https://leetcode.com/problems/escape-a-large-maze/

# @param {Integer[][]} blocked
# @param {Integer[]} source
# @param {Integer[]} target
# @return {Boolean}
def is_escape_possible(blocked, source, target)
  blocked_set = {}
  blocked.each { |b| blocked_set[b] = true }
  limit = blocked.length * (blocked.length - 1) / 2

  bfs = lambda do |start, goal|
    queue = [start.dup]
    seen = { start => true }
    until queue.empty?
      return true if seen.length > limit

      r, c = queue.shift
      return true if [r, c] == goal

      [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]].each do |nr, nc|
        next unless nr >= 0 && nr < 1_000_000 && nc >= 0 && nc < 1_000_000
        next if blocked_set[[nr, nc]] || seen[[nr, nc]]

        seen[[nr, nc]] = true
        queue << [nr, nc]
      end
    end
    false
  end

  bfs.call(source, target) && bfs.call(target, source)
end
