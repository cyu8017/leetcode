# LeetCode 1531 - String Compression II
# https://leetcode.com/problems/string-compression-ii/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def get_length_of_optimal_compression(s, k)
  memo = {}
  dp = lambda do |index, remaining|
    return 10**9 if remaining < 0
    return 0 if index == s.length || s.length - index <= remaining
    key = [index, remaining]
    return memo[key] if memo.key?(key)
    answer = dp.call(index + 1, remaining - 1)
    same = removed = 0
    (index...s.length).each do |j|
      if s[j] == s[index]
        same += 1
        encoded = 1 + (same >= 2 ? 1 : 0) + (same >= 10 ? 1 : 0) + (same >= 100 ? 1 : 0)
        answer = [answer, encoded + dp.call(j + 1, remaining - removed)].min
      else
        removed += 1
        break if removed > remaining
      end
    end
    memo[key] = answer
  end
  dp.call(0, k)
end
