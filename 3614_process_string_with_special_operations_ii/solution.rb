# LeetCode 3614 - Process String with Special Operations II
# https://leetcode.com/problems/process-string-with-special-operations-ii/

# @param {String} s
# @param {Integer} k
# @return {String}
def process_str(s, k)
  m = 0
  s.each_char do |c|
    if c == "*"
      m = m > 0 ? m - 1 : 0
    elsif c == "#"
      m <<= 1
    elsif c != "%"
      m += 1
    end
  end
  k2 = k
  return "." if k2 >= m

  i = s.length - 1
  loop do
    c = s[i]
    if c == "*"
      m += 1
    elsif c == "#"
      m /= 2
      k2 -= m if k2 >= m
    elsif c == "%"
      k2 = m - 1 - k2
    else
      m -= 1
      return c if k2 == m
    end
    i -= 1
  end
end
