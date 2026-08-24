# LeetCode 3561 - Resulting String After Adjacent Removals
# https://leetcode.com/problems/resulting-string-after-adjacent-removals/

# @param {String} s
# @return {String}
def resulting_string(s)
  is_contiguous = lambda do |a, b|
    x = (a.ord - b.ord).abs
    x == 1 || x == 25
  end
  stk = []
  s.each_char do |c|
    if !stk.empty? && is_contiguous.call(stk[-1], c)
      stk.pop
    else
      stk << c
    end
  end
  stk.join
end
