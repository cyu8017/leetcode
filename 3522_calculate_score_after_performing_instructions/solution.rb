# LeetCode 3522 - Calculate Score After Performing Instructions
# https://leetcode.com/problems/calculate-score-after-performing-instructions/

# @param {String[]} instructions
# @param {Integer[]} values
# @return {Integer}
def calculate_score(instructions, values)
  n = values.length
  vis = Array.new(n, false)
  ans = 0
  i = 0
  while i >= 0 && i < n && !vis[i]
    vis[i] = true
    if instructions[i][0] == "a"
      ans += values[i]
      i += 1
    else
      i += values[i]
    end
  end
  ans
end
