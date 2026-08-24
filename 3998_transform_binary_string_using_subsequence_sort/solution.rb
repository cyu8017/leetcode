# LeetCode 3998 - Transform Binary String Using Subsequence Sort
# https://leetcode.com/problems/transform-binary-string-using-subsequence-sort/

# @param {String} s
# @param {String[]} strs
# @return {Boolean[]}
def transform_str(s, strs)
  n = s.length
  prefix = Array.new(n + 1, 0)
  n.times { |i| prefix[i + 1] = prefix[i] + (s[i] == "1" ? 1 : 0) }
  result = Array.new(strs.length, false)
  strs.each_with_index do |t, i|
    left = 0
    right = 0
    ok = true
    n.times do |j|
      left += 1 if t[j] == "1"
      add = t[j] != "0" ? 1 : 0
      right += add
      right = prefix[j + 1] if right > prefix[j + 1]
      if left > right
        ok = false
        break
      end
    end
    result[i] = ok && left <= prefix[n] && prefix[n] <= right
  end
  result
end
