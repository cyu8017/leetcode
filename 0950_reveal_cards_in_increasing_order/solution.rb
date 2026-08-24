# LeetCode 0950 - Reveal Cards In Increasing Order
# https://leetcode.com/problems/reveal-cards-in-increasing-order/

# @param {Integer[]} deck
# @return {Integer[]}
def deck_revealed_increasing(deck)
  deck.sort!
  n = deck.length
  idx = (0...n).to_a
  ans = Array.new(n, 0)
  deck.each do |card|
    ans[idx.shift] = card
    idx << idx.shift unless idx.empty?
  end
  ans
end
