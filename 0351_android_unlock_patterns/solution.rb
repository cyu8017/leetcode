# LeetCode 0351 - Android Unlock Patterns
# https://leetcode.com/problems/android-unlock-patterns/

class Solution
  def number_of_patterns(m, n)
    jumps = {
      [0, 2] => 1, [2, 0] => 1,
      [0, 6] => 3, [6, 0] => 3,
      [0, 8] => 4, [8, 0] => 4,
      [2, 8] => 5, [8, 2] => 5,
      [2, 6] => 7, [6, 2] => 7,
      [6, 8] => 7, [8, 6] => 7,
      [1, 7] => 8, [7, 1] => 8,
      [3, 7] => 6, [7, 3] => 6,
      [1, 5] => 4, [5, 1] => 4,
      [3, 5] => 5, [5, 3] => 5,
      [1, 3] => 2, [3, 1] => 2,
      [4, 5] => 5, [5, 4] => 5,
      [4, 7] => 8, [7, 4] => 8,
      [4, 3] => 5, [3, 4] => 5,
      [4, 1] => 2, [1, 4] => 2,
      [4, 6] => 7, [6, 4] => 7,
      [4, 8] => 6, [8, 4] => 6,
      [4, 0] => 2, [0, 4] => 2,
      [4, 2] => 6, [2, 4] => 6
    }

    is_valid = lambda do |visited, last, next_cell|
      return false if visited & (1 << next_cell) != 0

      if jumps.key?([last, next_cell])
        return (visited & (1 << jumps[[last, next_cell]])) == 0
      end

      (last / 3 - next_cell / 3).abs <= 1 && (last % 3 - next_cell % 3).abs <= 1
    end

    dfs = lambda do |visited, last, length|
      return 0 if length > n

      count = (m <= length && length <= n) ? 1 : 0
      9.times do |next_cell|
        if is_valid.call(visited, last, next_cell)
          count += dfs.call(visited | (1 << next_cell), next_cell, length + 1)
        end
      end
      count
    end

    dfs.call(1 << 0, 0, 1) * 4 +
      dfs.call(1 << 1, 1, 1) * 4 +
      dfs.call(1 << 4, 4, 1)
  end

  alias_method :numberOfPatterns, :number_of_patterns
end
