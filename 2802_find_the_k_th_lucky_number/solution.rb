# LeetCode 2802 - Find The K-th Lucky Number
# https://leetcode.com/problems/find-the-k-th-lucky-number/

# @param {Integer} k
# @return {String}
def kth_lucky_number(k)
  k += 1
  bits = +""
  while k > 1
    bits = (k.even? ? "4" : "7") + bits
    k /= 2
  end
  bits
end
