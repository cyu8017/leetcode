# LeetCode 3461 - Check If Digits Are Equal in String After Operations I
# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

# @param {String} s
# @return {Boolean}
def has_same_digits(s)
  b = s.chars
  while b.length > 2
    nb = Array.new(b.length - 1, "")
    (0...(b.length - 1)).each do |i|
      nb[i] = ((b[i].ord - 48 + b[i + 1].ord - 48) % 10).to_s
    end
    b = nb
  end
  b[0] == b[1]
end
