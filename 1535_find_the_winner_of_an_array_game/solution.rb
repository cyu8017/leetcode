# LeetCode 1535 - Find the Winner of an Array Game
# https://leetcode.com/problems/find-the-winner-of-an-array-game/

# @param {Integer[]} arr
# @param {Integer} k
# @return {Integer}
def get_winner(arr, k)
  champion = arr[0]
  wins = 0
  arr[1..].each do |challenger|
    if champion > challenger
      wins += 1
    else
      champion = challenger
      wins = 1
    end
    break if wins == k
  end
  champion
end
