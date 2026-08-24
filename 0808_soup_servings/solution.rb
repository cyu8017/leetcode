# LeetCode 0808 - Soup Servings
# https://leetcode.com/problems/soup-servings/

# @param {Integer} n
# @return {Float}
def soup_servings(n)
  return 1.0 if n >= 4800

  units = (n + 24) / 25
  memo = {}
  dp = lambda do |a, b|
    key = [a, b]
    return memo[key] if memo.key?(key)
    return memo[key] = 0.5 if a <= 0 && b <= 0
    return memo[key] = 1.0 if a <= 0
    return memo[key] = 0.0 if b <= 0

    memo[key] = 0.25 * (
      dp.call(a - 4, b) +
      dp.call(a - 3, b - 1) +
      dp.call(a - 2, b - 2) +
      dp.call(a - 1, b - 3)
    )
  end

  dp.call(units, units)
end
