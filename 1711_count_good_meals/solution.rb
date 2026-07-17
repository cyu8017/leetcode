# LeetCode 1711 - Count Good Meals
# https://leetcode.com/problems/count-good-meals/

# @param {Integer[]} deliciousness
# @return {Integer}
def count_pairs(deliciousness)
  mod = 10**9 + 7
  seen = Hash.new(0)
  ans = 0
  deliciousness.each do |value|
    22.times do |power|
      ans += seen[(1 << power) - value]
    end
    seen[value] += 1
  end
  ans % mod
end
