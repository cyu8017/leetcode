# LeetCode 3340 - Check Balanced String
# https://leetcode.com/problems/check-balanced-string/

# @param {String} num
# @return {Boolean}
def is_balanced(num)
  even = 0
  odd = 0
  num.each_char.with_index do |ch, i|
    if i.even?
      even += ch.ord - 48
    else
      odd += ch.ord - 48
    end
  end
  even == odd
end
