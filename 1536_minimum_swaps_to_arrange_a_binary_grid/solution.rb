# LeetCode 1536 - Minimum Swaps to Arrange a Binary Grid
# https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/

# @param {Integer[][]} grid
# @return {Integer}
def min_swaps(grid)
  zeros = grid.map do |row|
    count = 0
    row.reverse_each do |value|
      break if value != 0
      count += 1
    end
    count
  end
  answer = 0
  n = grid.length
  (0...n).each do |i|
    required = n - i - 1
    j = i
    j += 1 while j < n && zeros[j] < required
    return -1 if j == n
    answer += j - i
    val = zeros[j]
    zeros.delete_at(j)
    zeros.insert(i, val)
  end
  answer
end
