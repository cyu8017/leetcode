# LeetCode 0764 - Largest Plus Sign
# https://leetcode.com/problems/largest-plus-sign/

# @param {Integer} n
# @param {Integer[][]} mines
# @return {Integer}
def order_of_largest_plus_sign(n, mines)
  banned = {}
  mines.each { |r, c| banned[r * n + c] = true }
  arms = Array.new(n) { Array.new(n, 0) }
  best = 0

  n.times do |r|
    count = 0
    n.times do |c|
      count = banned[r * n + c] ? 0 : count + 1
      arms[r][c] = count
    end
    count = 0
    (n - 1).downto(0) do |c|
      count = banned[r * n + c] ? 0 : count + 1
      arms[r][c] = [arms[r][c], count].min
    end
  end

  n.times do |c|
    count = 0
    n.times do |r|
      count = banned[r * n + c] ? 0 : count + 1
      arms[r][c] = [arms[r][c], count].min
    end
    count = 0
    (n - 1).downto(0) do |r|
      count = banned[r * n + c] ? 0 : count + 1
      arms[r][c] = [arms[r][c], count].min
      best = [best, arms[r][c]].max
    end
  end

  best
end
