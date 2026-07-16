# LeetCode 0087 - Scramble String
# https://leetcode.com/problems/scramble-string/

# @param {String} s1
# @param {String} s2
# @return {Boolean}
def is_scramble(s1, s2)
  memo = {}
  dfs = lambda do |a, b|
    key = "#{a}##{b}"
    return memo[key] if memo.key?(key)
    if a == b
      memo[key] = true
      return true
    end
    if a.chars.sort != b.chars.sort
      memo[key] = false
      return false
    end

    n = a.length
    (1...n).each do |i|
      if dfs.call(a[0, i], b[0, i]) && dfs.call(a[i..], b[i..])
        memo[key] = true
        return true
      end
      if dfs.call(a[0, i], b[-i..]) && dfs.call(a[i..], b[0, n - i])
        memo[key] = true
        return true
      end
    end
    memo[key] = false
    false
  end
  dfs.call(s1, s2)
end
