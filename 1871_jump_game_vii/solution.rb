# LeetCode 1871 - Jump Game VII
# https://leetcode.com/problems/jump-game-vii/

# @param {String} s
# @param {Integer} min_jump
# @param {Integer} max_jump
# @return {Boolean}
def can_reach(s, min_jump, max_jump)
  n = s.length
  reachable = Array.new(n, false)
  reachable[0] = true
  prefix = Array.new(n + 1, 0)

  (0...n).each do |i|
    if i > 0 && s[i] == "0"
      left = [0, i - max_jump].max
      right = i - min_jump
      if right >= left && prefix[right + 1] - prefix[left] > 0
        reachable[i] = true
      end
    end
    prefix[i + 1] = prefix[i] + (reachable[i] ? 1 : 0)
  end

  reachable[n - 1]
end
