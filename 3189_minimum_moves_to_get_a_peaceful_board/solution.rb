# LeetCode 3189 - Minimum Moves to Get a Peaceful Board
# https://leetcode.com/problems/minimum-moves-to-get-a-peaceful-board/

# @param {Integer[][]} rooks
# @return {Integer}
def min_moves(rooks)
  ans = 0
  rooks.sort_by! { |a| a[0] }
  rooks.each_with_index { |r, i| ans += (r[0] - i).abs }
  rooks.sort_by! { |a| a[1] }
  rooks.each_with_index { |r, j| ans += (r[1] - j).abs }
  ans
end
