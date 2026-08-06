# LeetCode 1492 - The Kth Factor Of N
# https://leetcode.com/problems/the-kth-factor-of-n/

def kth_factor(n, k)
  (1..n).each do |x|
    next unless n % x == 0
    k -= 1
    return x if k == 0
  end
  -1
end
