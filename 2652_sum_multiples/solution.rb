# LeetCode 2652 - Sum Multiples
# https://leetcode.com/problems/sum-multiples/

# @param {Integer} n
# @return {Integer}
def sum_of_multiples(n)
  ans = 0
  (1..n).each { |i| ans += i if i % 3 == 0 || i % 5 == 0 || i % 7 == 0 }
  ans
end
