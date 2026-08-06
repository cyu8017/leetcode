# LeetCode 1945 - Sum of Digits of String After Convert
# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def get_lucky(s, k)
  num = s.chars.map { |c| (c.ord - 96).to_s }.join
  k.times { num = num.chars.map(&:to_i).sum.to_s }
  num.to_i
end
