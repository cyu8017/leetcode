# LeetCode 3664 - Two-Letter Card Game
# https://leetcode.com/problems/two-letter-card-game/

# @param {String[]} cards
# @param {String} x
# @return {Integer}
def score(cards, x)
  pair_group = lambda do |arr|
    total = 0
    mx = 0
    26.times do |i|
      total += arr[i]
      mx = arr[i] if arr[i] > mx
    end
    pairs = total / 2
    pairs = total - mx if total - mx < pairs
    [pairs, total - 2 * pairs]
  end
  xx = 0
  left = Array.new(26, 0)
  right = Array.new(26, 0)
  cards.each do |c|
    a = c[0]
    b = c[1]
    if a == x && b == x
      xx += 1
    elsif a == x
      left[b.ord - 97] += 1
    elsif b == x
      right[a.ord - 97] += 1
    end
  end
  lp = pair_group.call(left)
  rp = pair_group.call(right)
  ans = lp[0] + rp[0]
  rem = lp[1] + rp[1]
  use = [xx, rem].min
  ans += use
  xx -= use
  ans + xx / 2
end
