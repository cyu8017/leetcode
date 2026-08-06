# LeetCode 1583 - Count Unhappy Friends
# https://leetcode.com/problems/count-unhappy-friends/

# @param {Integer} n
# @param {Integer[][]} preferences
# @param {Integer[][]} pairs
# @return {Integer}
def unhappy_friends(n, preferences, pairs)
  rank = preferences.map do |pref|
    pref.each_with_index.to_h { |friend, i| [friend, i] }
  end
  partner = {}
  pairs.each do |a, b|
    partner[a] = b
    partner[b] = a
  end
  unhappy = 0
  (0...n).each do |x|
    y = partner[x]
    prefs = preferences[x][0...rank[x][y]]
    unhappy += 1 if prefs.any? { |u| rank[u][x] < rank[u][partner[u]] }
  end
  unhappy
end
