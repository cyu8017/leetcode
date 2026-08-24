# LeetCode 2551 - Put Marbles in Bags
# https://leetcode.com/problems/put-marbles-in-bags/

# @param {Integer[]} weights
# @param {Integer} k
# @return {Integer}
def put_marbles(weights, k)
  n = weights.length
  return 0 if k == 1 || k == n

  pair = (0...n - 1).map { |i| weights[i] + weights[i + 1] }
  pair.sort!
  mn = 0
  mx = 0
  (k - 1).times do |i|
    mn += pair[i]
    mx += pair[n - 2 - i]
  end
  mx - mn
end
