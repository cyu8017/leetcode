# LeetCode 3963 - Create Grid With Exactly One Path
# https://leetcode.com/problems/create-grid-with-exactly-one-path/

# @param {Integer} m
# @param {Integer} n
# @return {String[]}
def create_grid(m, n)
  g = []
  m.times do |i|
    row = Array.new(n, "#")
    n.times { |j| row[j] = "." } if i == 0
    row[n - 1] = "."
    g << row.join
  end
  g
end
