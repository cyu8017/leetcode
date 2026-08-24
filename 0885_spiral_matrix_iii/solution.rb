# LeetCode 0885 - Spiral Matrix III
# https://leetcode.com/problems/spiral-matrix-iii/

# @param {Integer} rows
# @param {Integer} cols
# @param {Integer} r_start
# @param {Integer} c_start
# @return {Integer[][]}
def spiral_matrix_iii(rows, cols, r_start, c_start)
  ans = [[r_start, c_start]]
  return ans if rows * cols == 1

  r = r_start
  c = c_start
  dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  steps = 1
  while ans.length < rows * cols
    4.times do |d|
      dr, dc = dirs[d]
      steps.times do
        r += dr
        c += dc
        if r >= 0 && r < rows && c >= 0 && c < cols
          ans << [r, c]
          return ans if ans.length == rows * cols
        end
      end
      steps += 1 if d.odd?
    end
  end
  ans
end
