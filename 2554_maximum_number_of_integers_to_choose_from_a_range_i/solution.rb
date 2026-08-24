# LeetCode 2554 - Maximum Number of Integers to Choose From a Range I
# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

# @param {Integer[]} banned
# @param {Integer} n
# @param {Integer} max_sum
# @return {Integer}
def max_count(banned, n, max_sum)
  ban = {}
  banned.each { |x| ban[x] = true }
  ans = 0
  s = 0
  (1..n).each do |i|
    next if ban[i]
    break if s + i > max_sum

    s += i
    ans += 1
  end
  ans
end
