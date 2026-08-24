# LeetCode 3758 - Convert Number Words to Digits
# https://leetcode.com/problems/convert-number-words-to-digits/

# @param {String} s
# @return {String}
def convert_number(s)
  d = %w[zero one two three four five six seven eight nine]
  n = s.length
  ans = []
  i = 0
  while i < n
    (0...10).each do |j|
      m = d[j].length
      if i + m <= n && s[i, m] == d[j]
        ans << (48 + j).chr
        i += m - 1
        break
      end
    end
    i += 1
  end
  ans.join
end
