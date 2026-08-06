# LeetCode 1387 - Sort Integers By The Power Value
# https://leetcode.com/problems/sort-integers-by-the-power-value/

def get_kth(lo, hi, k)
  memo = {}
  power = lambda do |x|
    return memo[x] if memo.key?(x)
    memo[x] = x == 1 ? 0 : 1 + power.call(x.even? ? x / 2 : 3 * x + 1)
  end
  (lo..hi).sort_by { |x| [power.call(x), x] }[k - 1]
end
