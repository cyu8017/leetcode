# LeetCode 1306 - Jump Game Iii
# https://leetcode.com/problems/jump-game-iii/

def can_reach(arr, start)
  stack = [start]
  seen = {}
  while !stack.empty?
    i = stack.pop
    next if seen[i] || i < 0 || i >= arr.length
    return true if arr[i] == 0
    seen[i] = true
    stack << i - arr[i] << i + arr[i]
  end
  false
end
