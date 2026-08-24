# LeetCode 3752 - Lexicographically Smallest Negated Permutation That Sums to Target
# https://leetcode.com/problems/lexicographically-smallest-negated-permutation-that-sums-to-target/

# @param {Integer} n
# @param {Integer} target
# @return {Integer[]}
def lexicographically_smallest(n, target)
  total = n * (n + 1) / 2
  return [] if target < -total || target > total || (total - target).odd?
  remaining = (total - target) / 2
  negative = Array.new(n + 1, false)
  n.downto(1) do |value|
    if value <= remaining
      negative[value] = true
      remaining -= value
    end
  end
  answer = []
  n.downto(1) { |value| answer << -value if negative[value] }
  (1..n).each { |value| answer << value unless negative[value] }
  answer
end
