# LeetCode 3248 - Snake in Matrix
# https://leetcode.com/problems/snake-in-matrix/

# @param {Integer} n
# @param {String[]} commands
# @return {Integer}
def final_position_of_snake(n, commands)
  x = y = 0
  commands.each do |c|
    case c[0]
    when "U" then x -= 1
    when "D" then x += 1
    when "L" then y -= 1
    when "R" then y += 1
    end
  end
  x * n + y
end
