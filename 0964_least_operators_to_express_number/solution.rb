# LeetCode 0964 - Least Operators to Express Number
# https://leetcode.com/problems/least-operators-to-express-number/

# @param {Integer} x
# @param {Integer} target
# @return {Integer}
def least_ops_express_target(x, target)
  memo = {}
  dfs = lambda do |t|
    return memo[t] if memo.key?(t)
    return memo[t] = [2 * t - 1, 2 * (x - t)].min if x > t
    return memo[t] = 0 if x == t

    prod = x
    n = 0
    while prod < t
      prod *= x
      n += 1
    end
    return memo[t] = n if prod == t

    ans = dfs.call(t - prod / x) + n
    ans = [ans, dfs.call(prod - t) + n + 1].min if prod < 2 * t
    memo[t] = ans
  end
  dfs.call(target)
end
