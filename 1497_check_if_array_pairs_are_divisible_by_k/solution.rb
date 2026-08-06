# LeetCode 1497 - Check If Array Pairs Are Divisible By K
# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

def can_arrange(arr, k)
  count = Hash.new(0)
  arr.each { |x| count[((x % k) + k) % k] += 1 }
  return false if count[0].odd?
  (1...k).all? { |r| count[r] == count[k - r] }
end
