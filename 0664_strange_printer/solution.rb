# LeetCode 0664 - Strange Printer
# https://leetcode.com/problems/strange-printer/

# @param {String} s
# @return {Integer}
def strange_printer(s)
  memo = {}

  dfs = lambda do |i, j|
    return 0 if i > j

    key = [i, j]
    return memo[key] if memo.key?(key)

    ans = dfs.call(i + 1, j) + 1
    ((i + 1)..j).each do |k|
      ans = [ans, dfs.call(i, k - 1) + dfs.call(k + 1, j)].min if s[k] == s[i]
    end
    memo[key] = ans
  end

  dfs.call(0, s.length - 1)
end
