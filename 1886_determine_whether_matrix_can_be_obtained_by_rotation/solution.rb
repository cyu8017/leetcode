# LeetCode 1886 - Determine Whether Matrix Can Be Obtained By Rotation
# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

# @param {Integer[][]} mat
# @param {Integer[][]} target
# @return {Boolean}
def find_rotation(mat, target)
  current = mat
  4.times do
    return true if current == target

    n = current.length
    current = (0...n).map { |col| (0...n).map { |row| current[n - 1 - row][col] } }
  end
  false
end
