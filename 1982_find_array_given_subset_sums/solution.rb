# LeetCode 1982 - Find Array Given Subset Sums
# https://leetcode.com/problems/find-array-given-subset-sums/

# @param {Integer} n
# @param {Integer[]} sums
# @return {Integer[]}
def recover_array(n, sums)
  sums = sums.sort
  ans = []
  n.times do
    d = sums[1] - sums[0]
    count = Hash.new(0)
    sums.each { |x| count[x] += 1 }
    without = []
    with_d = []
    sums.each do |x|
      next if count[x].zero?
      count[x] -= 1
      count[x + d] -= 1
      without << x
      with_d << x + d
    end
    if without.include?(0)
      ans << d
      sums = without
    else
      ans << -d
      sums = with_d
    end
  end
  ans
end
