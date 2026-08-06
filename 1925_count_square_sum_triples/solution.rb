# LeetCode 1925 - Count Square Sum Triples
# https://leetcode.com/problems/count-square-sum-triples/

# @param {Integer} n
# @return {Integer}
def count_triples(n)
  squares = {}
  (1..n).each { |i| squares[i * i] = true }
  ans = 0
  (1..n).each do |a|
    (1..n).each do |b|
      ans += 1 if squares[a * a + b * b]
    end
  end
  ans
end
