# LeetCode 2561 - Rearranging Fruits
# https://leetcode.com/problems/rearranging-fruits/

# @param {Integer[]} basket1
# @param {Integer[]} basket2
# @return {Integer}
def min_cost(basket1, basket2)
  freq = Hash.new(0)
  mn = Float::INFINITY
  basket1.each do |x|
    freq[x] += 1
    mn = x if x < mn
  end
  basket2.each do |x|
    freq[x] -= 1
    mn = x if x < mn
  end
  extra = []
  freq.each do |key, v|
    return -1 if v.odd?

    (v.abs / 2).times { extra << key }
  end
  extra.sort!
  ans = 0
  (extra.length / 2).times do |i|
    cand = extra[i]
    twice = 2 * mn
    ans += cand < twice ? cand : twice
  end
  ans
end
