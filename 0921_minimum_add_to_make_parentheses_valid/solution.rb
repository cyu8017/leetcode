# LeetCode 0921 - Minimum Add to Make Parentheses Valid
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

# @param {String} s
# @return {Integer}
def min_add_to_make_valid(s)
  open_need = close_need = 0
  s.each_char do |ch|
    if ch == "("
      close_need += 1
    elsif close_need > 0
      close_need -= 1
    else
      open_need += 1
    end
  end
  open_need + close_need
end
