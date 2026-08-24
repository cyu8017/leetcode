# LeetCode 2347 - Best Poker Hand
# https://leetcode.com/problems/best-poker-hand/

# @param {Integer[]} ranks
# @param {String[]} suits
# @return {String}
def best_hand(ranks, suits)
  return "Flush" if suits[0] == suits[1] && suits[1] == suits[2] && suits[2] == suits[3] && suits[3] == suits[4]
  cnt = Hash.new(0)
  best = 0
  ranks.each do |r|
    cnt[r] += 1
    best = cnt[r] if cnt[r] > best
  end
  return "Three of a Kind" if best >= 3
  return "Pair" if best == 2
  "High Card"
end
