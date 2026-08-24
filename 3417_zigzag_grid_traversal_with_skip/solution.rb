# LeetCode 3417 - Zigzag Grid Traversal With Skip
# https://leetcode.com/problems/zigzag-grid-traversal-with-skip/

# @param {Integer[][]} grid
# @return {Integer[]}
def zigzag_traversal(grid)
  ans = []
  skip = false
  grid.each_with_index do |row, i|
    if i.even?
      row.each do |v|
        ans << v unless skip
        skip = !skip
      end
    else
      (row.length - 1).downto(0) do |j|
        ans << row[j] unless skip
        skip = !skip
      end
    end
  end
  ans
end
