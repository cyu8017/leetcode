# LeetCode 3116 - Kth Smallest Amount With Single Denomination Combination
# https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/

# @param {Integer[]} coins
# @param {Integer} k
# @return {Integer}
def find_kth_smallest(coins, k)
  gcdll = lambda do |a, b|
    a, b = b, a % b while b != 0
    a
  end
  lcmll = lambda { |a, b| a / gcdll.call(a, b) * b }
  bit_count = lambda do |x|
    c = 0
    while x != 0
      c += x & 1
      x >>= 1
    end
    c
  end
  n = coins.length

  check = lambda do |mx|
    cnt = 0
    (1...(1 << n)).each do |i|
      v = 1
      n.times do |j|
        if ((i >> j) & 1) != 0
          v = lcmll.call(v, coins[j])
          break if v > mx
        end
      end
      m = bit_count.call(i)
      if m.odd?
        cnt += mx / v
      else
        cnt -= mx / v
      end
    end
    cnt >= k
  end

  lo = 1
  hi = 100_000_000_000
  while lo < hi
    mid = lo + (hi - lo) / 2
    if check.call(mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
