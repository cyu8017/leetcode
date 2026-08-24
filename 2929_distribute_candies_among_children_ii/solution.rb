# LeetCode 2929 - Distribute Candies Among Children II
# https://leetcode.com/problems/distribute-candies-among-children-ii/

# @param {Integer} n
# @param {Integer} limit
# @return {Integer}
def distribute_candies(n, limit)
  comb2 = lambda do |x|
    return 0 if x < 0

    (x + 1) * (x + 2) / 2
  end

  ans = comb2.call(n)
  ans -= 3 * comb2.call(n - (limit + 1))
  ans += 3 * comb2.call(n - 2 * (limit + 1))
  ans -= comb2.call(n - 3 * (limit + 1))
  ans
end
