# LeetCode 2513 - Minimize the Maximum of Two Arrays
# https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

# @param {Integer} divisor1
# @param {Integer} divisor2
# @param {Integer} unique_cnt1
# @param {Integer} unique_cnt2
# @return {Integer}
def minimize_set(divisor1, divisor2, unique_cnt1, unique_cnt2)
  gcd = lambda do |a, b|
    while b != 0
      a, b = b, a % b
    end
    a
  end

  lcm = (divisor1 / gcd.call(divisor1, divisor2)) * divisor2
  ok = lambda do |x|
    a = x - x / divisor1
    b = x - x / divisor2
    both = x - x / lcm
    a >= unique_cnt1 && b >= unique_cnt2 && both >= unique_cnt1 + unique_cnt2
  end

  lo = 1
  hi = 2**62
  while lo < hi
    mid = (lo + hi) / 2
    if ok.call(mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
