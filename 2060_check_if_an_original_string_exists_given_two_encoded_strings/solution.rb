# LeetCode 2060 - Check if an Original String Exists Given Two Encoded Strings
# https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/

# @param {String} s1
# @param {String} s2
# @return {Boolean}
def possibly_equals(s1, s2)
  memo = {}
  n = s1.length
  m = s2.length
  is_digit = ->(c) { !c.nil? && c >= "0" && c <= "9" }

  dfs = lambda do |i, j, diff|
    key = [i, j, diff]
    next memo[key] if memo.key?(key)

    if i == n && j == m
      memo[key] = diff.zero?
      next diff.zero?
    end
    res = false
    if i < n && is_digit.call(s1[i])
      val = 0
      pos = i
      while pos < n && is_digit.call(s1[pos])
        val = val * 10 + (s1[pos].ord - 48)
        if dfs.call(pos + 1, j, diff + val)
          res = true
          break
        end
        pos += 1
      end
    elsif j < m && is_digit.call(s2[j])
      val = 0
      pos = j
      while pos < m && is_digit.call(s2[pos])
        val = val * 10 + (s2[pos].ord - 48)
        if dfs.call(i, pos + 1, diff - val)
          res = true
          break
        end
        pos += 1
      end
    elsif diff.positive?
      res = j < m && dfs.call(i, j + 1, diff - 1)
    elsif diff.negative?
      res = i < n && dfs.call(i + 1, j, diff + 1)
    else
      res = i < n && j < m && s1[i] == s2[j] && dfs.call(i + 1, j + 1, 0)
    end
    memo[key] = res
    res
  end
  dfs.call(0, 0, 0)
end
