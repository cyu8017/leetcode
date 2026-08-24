# LeetCode 3898 - Find the Degree of Each Vertex
# https://leetcode.com/problems/find-the-degree-of-each-vertex/

# @param {Integer[][]} matrix
# @return {Integer[]}
def find_degrees(matrix)
  ans = Array.new(matrix.length, 0)
  matrix.each_with_index do |row, i|
    row.each { |x| ans[i] += x }
  end
  ans
end
