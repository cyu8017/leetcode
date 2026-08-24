# LeetCode 2606 - Find the Substring With Maximum Cost
# https://leetcode.com/problems/find-the-substring-with-maximum-cost/

# @param {String} s
# @param {String} chars
# @param {Integer[]} vals
# @return {Integer}
def maximum_cost_substring(s, chars, vals)
  val = (1..26).to_a
  chars.each_char.with_index { |ch, i| val[ch.ord - 97] = vals[i] }
  best = 0
  cur = 0
  s.each_char do |c|
    cur += val[c.ord - 97]
    cur = 0 if cur < 0
    best = cur if cur > best
  end
  best
end
