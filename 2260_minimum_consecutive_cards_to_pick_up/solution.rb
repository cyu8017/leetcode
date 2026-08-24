# LeetCode 2260 - Minimum Consecutive Cards to Pick Up
# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

# @param {Integer[]} cards
# @return {Integer}
def minimum_card_pickup(cards)
  last = {}
  ans = -1
  cards.each_with_index do |x, i|
    if last.key?(x)
      diff = i - last[x] + 1
      ans = diff if ans == -1 || diff < ans
    end
    last[x] = i
  end
  ans
end
