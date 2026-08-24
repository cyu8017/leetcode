# LeetCode 0661 - Image Smoother
# https://leetcode.com/problems/image-smoother/

# @param {Integer[][]} img
# @return {Integer[][]}
def image_smoother(img)
  m = img.length
  n = img[0].length
  out = Array.new(m) { Array.new(n, 0) }
  m.times do |i|
    n.times do |j|
      total = 0
      count = 0
      [-1, 0, 1].each do |di|
        [-1, 0, 1].each do |dj|
          ni = i + di
          nj = j + dj
          if ni >= 0 && ni < m && nj >= 0 && nj < n
            total += img[ni][nj]
            count += 1
          end
        end
      end
      out[i][j] = total / count
    end
  end
  out
end
