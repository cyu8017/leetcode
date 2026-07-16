# LeetCode 0062 - Unique Paths
# https://leetcode.com/problems/unique-paths/

# @param {Integer} m
# @param {Integer} n
# @return {Integer}
def unique_paths(m, n)
  row = Array.new(n, 1)

  (1...m).each do
    (1...n).each do |col|
      row[col] += row[col - 1]
    end
  end

  row[n - 1]
end
