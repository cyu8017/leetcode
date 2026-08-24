# LeetCode 3579 - Minimum Steps to Convert String with Operations
# https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/

# @param {String} word1
# @param {String} word2
# @return {Integer}
def min_operations(word1, word2)
  calc = lambda do |l, r, rev|
    cnt = Array.new(26) { Array.new(26, 0) }
    res = 0
    (l..r).each do |i|
      j = rev ? r - (i - l) : i
      a = word1[j].ord - 97
      b = word2[i].ord - 97
      if a != b
        if cnt[b][a] > 0
          cnt[b][a] -= 1
        else
          cnt[a][b] += 1
          res += 1
        end
      end
    end
    res
  end
  n = word1.length
  f = Array.new(n + 1, 2147483647 / 2)
  f[0] = 0
  (1..n).each do |i|
    (0...i).each do |j|
      a = calc.call(j, i - 1, false)
      b = 1 + calc.call(j, i - 1, true)
      f[i] = [f[i], f[j] + [a, b].min].min
    end
  end
  f[n]
end
