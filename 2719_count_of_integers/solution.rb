# LeetCode 2719 - Count of Integers
# https://leetcode.com/problems/count-of-integers/

# @param {String} num1
# @param {String} num2
# @param {Integer} min_sum
# @param {Integer} max_sum
# @return {Integer}
def count(num1, num2, min_sum, max_sum)
  mod = 1_000_000_007
  dec = lambda do |s|
    arr = s.chars
    i = arr.length - 1
    while i >= 0 && arr[i] == "0"
      arr[i] = "9"
      i -= 1
    end
    arr[i] = (arr[i].ord - 1).chr if i >= 0
    j = 0
    j += 1 while j < arr.length - 1 && arr[j] == "0"
    arr[j..].join
  end
  dp = lambda do |s|
    memo = {}
    dfs = nil
    dfs = lambda do |pos, sm, tight|
      return 0 if sm > max_sum
      return sm >= min_sum ? 1 : 0 if pos == s.length

      key = [pos, sm, tight]
      return memo[key] if memo.key?(key)

      up = tight ? s[pos].ord - 48 : 9
      res = 0
      (0..up).each do |d|
        res = (res + dfs.call(pos + 1, sm + d, tight && d == up)) % mod
      end
      memo[key] = res
      res
    end
    dfs.call(0, 0, true)
  end
  (dp.call(num2) - dp.call(dec.call(num1)) + mod) % mod
end
