# LeetCode 2029 - Stone Game IX
# https://leetcode.com/problems/stone-game-ix/

# @param {Integer[]} stones
# @return {Boolean}
def stone_game_ix(stones)
  cnt = [0, 0, 0]
  stones.each { |s| cnt[s % 3] += 1 }
  if cnt[0].even?
    cnt[1] > 0 && cnt[2] > 0
  else
    (cnt[1] - cnt[2]).abs > 2
  end
end
