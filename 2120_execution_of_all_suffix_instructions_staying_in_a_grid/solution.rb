# LeetCode 2120 - Execution of All Suffix Instructions Staying in a Grid
# https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/

# @param {Integer} n
# @param {Integer[]} start_pos
# @param {String} s
# @return {Integer[]}
def execute_instructions(n, start_pos, s)
  m = s.length
  ans = Array.new(m, 0)
  m.times do |i|
    r = start_pos[0]
    c = start_pos[1]
    cnt = 0
    (i...m).each do |j|
      ch = s[j]
      case ch
      when "L" then c -= 1
      when "R" then c += 1
      when "U" then r -= 1
      else r += 1
      end
      break if r < 0 || r >= n || c < 0 || c >= n

      cnt += 1
    end
    ans[i] = cnt
  end
  ans
end
