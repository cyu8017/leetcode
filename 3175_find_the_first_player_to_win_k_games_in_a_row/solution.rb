# LeetCode 3175 - Find The First Player to win K Games in a Row
# https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/

# @param {Integer[]} skills
# @param {Integer} k
# @return {Integer}
def find_winning_player(skills, k)
  n = skills.length
  k = [k, n - 1].min
  i = 0
  cnt = 0
  (1...n).each do |j|
    if skills[i] < skills[j]
      i = j
      cnt = 1
    else
      cnt += 1
    end
    break if cnt == k
  end
  i
end
