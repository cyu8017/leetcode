# LeetCode 0914 - X of a Kind in a Deck of Cards
# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

# @param {Integer[]} deck
# @return {Boolean}
def has_groups_size_x(deck)
  counts = Hash.new(0)
  deck.each { |x| counts[x] += 1 }
  g = counts.values.reduce { |a, b| a.gcd(b) }
  g >= 2
end
