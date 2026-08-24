# LeetCode 3030 - Find the Grid of Region Average
# https://leetcode.com/problems/find-the-grid-of-region-average/

# @param {Integer[][]} image
# @param {Integer} threshold
# @return {Integer[][]}
def result_grid(image, threshold)
  n = image.length
  m = image[0].length
  ans = Array.new(n) { Array.new(m, 0) }
  ct = Array.new(n) { Array.new(m, 0) }
  (0...n - 2).each do |i|
    (0...m - 2).each do |j|
      region = true
      3.times do |k|
        2.times do |l|
          region &&= (image[i + k][j + l] - image[i + k][j + l + 1]).abs <= threshold
        end
      end
      2.times do |k|
        3.times do |l|
          region &&= (image[i + k][j + l] - image[i + k + 1][j + l]).abs <= threshold
        end
      end
      next unless region

      tot = 0
      3.times { |k| 3.times { |l| tot += image[i + k][j + l] } }
      3.times do |k|
        3.times do |l|
          ct[i + k][j + l] += 1
          ans[i + k][j + l] += tot / 9
        end
      end
    end
  end
  n.times do |i|
    m.times do |j|
      ans[i][j] = if ct[i][j] == 0
                    image[i][j]
                  else
                    ans[i][j] / ct[i][j]
                  end
    end
  end
  ans
end
