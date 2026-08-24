# LeetCode 3360 - Stone Removal Game
# https://leetcode.com/problems/stone-removal-game/

# @param {Integer} n
# @return {Boolean}
def can_alice_win(n)
  take = 10
  alice = true
  while n >= take && take > 0
    n -= take
    take -= 1
    alice = !alice
  end
  !alice
end
