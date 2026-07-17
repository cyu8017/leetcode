# LeetCode 1735 - Count Ways to Make Array With Product
# https://leetcode.com/problems/count-ways-to-make-array-with-product/

# @param {Integer[][]} queries
# @return {Integer[]}
def ways_to_fill_array(queries)
  mod = 10**9 + 7
  comb = lambda do |a, b|
    result = 1
    (1..b).each { |i| result = result * (a - b + i) / i }
    result
  end
  queries.map do |n, k|
    ways = 1
    d = 2
    value = k
    while d * d <= value
      if value % d == 0
        exp = 0
        while value % d == 0
          value /= d
          exp += 1
        end
        ways = ways * comb.call(n + exp - 1, exp) % mod
      end
      d += d == 2 ? 1 : 2
    end
    ways = ways * n % mod if value > 1
    ways
  end
end
