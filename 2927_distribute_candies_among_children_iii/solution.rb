# LeetCode 2927 - Distribute Candies Among Children III
# https://leetcode.com/problems/distribute-candies-among-children-iii/

# @param {Integer} n
# @param {Integer} limit
# @return {Integer}
def distribute_candies(n, limit)
  comb = lambda do |x|
    return 0 if x < 2

    x * (x - 1) / 2
  end

  ans = comb.call(n + 2)
  ans -= 3 * comb.call(n - limit + 1)
  ans += 3 * comb.call(n - 2 * (limit + 1) + 2)
  ans -= comb.call(n - 3 * (limit + 1) + 2)
  ans = 0 if ans < 0
  ans
end
