# LeetCode 2217 - Find Palindrome With Fixed Length
# https://leetcode.com/problems/find-palindrome-with-fixed-length/

# @param {Integer[]} queries
# @param {Integer} int_length
# @return {Integer[]}
def kth_palindrome(queries, int_length)
  half = (int_length + 1) >> 1
  start = 1
  (1...half).each { start *= 10 }
  total = start * 9
  ans = Array.new(queries.length)
  queries.each_with_index do |q, i|
    if q > total
      ans[i] = -1
      next
    end
    left = start + q - 1
    pal = left
    x = left
    x /= 10 if int_length.odd?
    while x > 0
      pal = pal * 10 + x % 10
      x /= 10
    end
    ans[i] = pal
  end
  ans
end
