# LeetCode 3238 - Find the Number of Winning Players
# https://leetcode.com/problems/find-the-number-of-winning-players/

# @param {Integer} n
# @param {Integer[][]} pick
# @return {Integer}
def winning_player_count(n, pick)
  cnt = Array.new(n) { Array.new(11, 0) }
  s = {}
  pick.each do |p|
    x = p[0]
    y = p[1]
    cnt[x][y] += 1
    s[x] = true if cnt[x][y] > x
  end
  s.length
end
