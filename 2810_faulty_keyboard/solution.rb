# LeetCode 2810 - Faulty Keyboard
# https://leetcode.com/problems/faulty-keyboard/

# @param {String} s
# @return {String}
def final_string(s)
  b = +""
  s.each_char do |c|
    if c == "i"
      b.reverse!
    else
      b << c
    end
  end
  b
end
