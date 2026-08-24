# LeetCode 0672 - Bulb Switcher II
# https://leetcode.com/problems/bulb-switcher-ii/

# @param {Integer} n
# @param {Integer} presses
# @return {Integer}
def flip_lights(n, presses)
  n = [n, 3].min
  return 1 if presses.zero?
  return [2, 3, 4][n - 1] if presses == 1
  return [2, 4, 7][n - 1] if presses == 2

  [2, 4, 8][n - 1]
end
