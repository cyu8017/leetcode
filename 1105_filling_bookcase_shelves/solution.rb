# LeetCode 1105 - Filling Bookcase Shelves
# https://leetcode.com/problems/filling-bookcase-shelves/

# @param {Integer[][]} books
# @param {Integer} shelf_width
# @return {Integer}
def min_height_shelves(books, shelf_width)
  n = books.length
  dp = Array.new(n + 1, 0)
  (1..n).each do |i|
    width = 0
    height = 0
    dp[i] = Float::INFINITY
    i.downto(1) do |j|
      w, h = books[j - 1]
      width += w
      break if width > shelf_width
      height = [height, h].max
      dp[i] = [dp[i], dp[j - 1] + height].min
    end
  end
  dp[n]
end
