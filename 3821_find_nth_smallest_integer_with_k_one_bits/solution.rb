# LeetCode 3821 - Find Nth Smallest Integer with K One Bits
# https://leetcode.com/problems/find-nth-smallest-integer-with-k-one-bits/

# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def nth_smallest(n, k)
  mx = 50
  c = Array.new(mx) { Array.new(mx + 1, 0) }
  (0...mx).each do |i|
    c[i][0] = 1
    (1..i).each { |j| c[i][j] = c[i - 1][j - 1] + c[i - 1][j] }
  end
  ans = 0
  nn = n
  49.downto(0) do |i|
    if k >= 0 && nn > c[i][k]
      nn -= c[i][k]
      ans |= 1 << i
      k -= 1
      break if k == 0
    end
  end
  ans
end
