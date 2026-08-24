# LeetCode 0733 - Flood Fill
# https://leetcode.com/problems/flood-fill/

# @param {Integer[][]} image
# @param {Integer} sr
# @param {Integer} sc
# @param {Integer} color
# @return {Integer[][]}
def flood_fill(image, sr, sc, color)
  original = image[sr][sc]
  return image if original == color

  m = image.length
  n = image[0].length
  dfs = lambda do |r, c|
    return if r < 0 || r >= m || c < 0 || c >= n || image[r][c] != original

    image[r][c] = color
    dfs.call(r + 1, c)
    dfs.call(r - 1, c)
    dfs.call(r, c + 1)
    dfs.call(r, c - 1)
  end
  dfs.call(sr, sc)
  image
end
