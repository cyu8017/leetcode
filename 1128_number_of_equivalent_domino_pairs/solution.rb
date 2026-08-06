# LeetCode 1128 - Number of Equivalent Domino Pairs
# https://leetcode.com/problems/number-of-equivalent-domino-pairs/

# @param {Integer[][]} dominoes
# @return {Integer}
def num_equiv_domino_pairs(dominoes)
  count = Hash.new(0)
  ans = 0
  dominoes.each do |a, b|
    key = a < b ? a * 10 + b : b * 10 + a
    ans += count[key]
    count[key] += 1
  end
  ans
end
