# LeetCode 1556 - Thousand Separator
# https://leetcode.com/problems/thousand-separator/

# @param {Integer} n
# @return {String}
def thousand_separator(n)
  s = n.to_s
  parts = []
  until s.empty?
    parts << s[[s.length - 3, 0].max..]
    s = s[0...[s.length - 3, 0].max]
  end
  parts.reverse.join('.')
end
