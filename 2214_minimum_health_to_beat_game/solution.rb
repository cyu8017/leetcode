# LeetCode 2214 - Minimum Health to Beat Game
# https://leetcode.com/problems/minimum-health-to-beat-game/

# @param {Integer[]} damage
# @param {Integer} armor
# @return {Integer}
def minimum_health(damage, armor)
  sum = 0
  mx = 0
  damage.each do |d|
    sum += d
    mx = [mx, d].max
  end
  sum - [armor, mx].min + 1
end

alias solve minimum_health
