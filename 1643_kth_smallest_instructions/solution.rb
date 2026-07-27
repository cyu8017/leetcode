# LeetCode 1643 - Kth Smallest Instructions
# https://leetcode.com/problems/kth-smallest-instructions/

def _comb_1643(n, k)
  return 0 if k < 0 || k > n
  return 1 if k.zero? || k == n

  k = n - k if k > n - k
  res = 1
  (1..k).each { |i| res = res * (n - k + i) / i }
  res
end

# @param {Integer[]} destination
# @param {Integer} k
# @return {String}
def kth_smallest_path(destination, k)
  v, h = destination
  ans = []
  while h + v > 0
    if h.positive?
      count = _comb_1643(h + v - 1, v)
      if k <= count
        ans << "H"
        h -= 1
        next
      end
      k -= count
    end
    ans << "V"
    v -= 1
  end
  ans.join
end
