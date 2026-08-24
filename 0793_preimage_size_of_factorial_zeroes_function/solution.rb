# LeetCode 0793 - Preimage Size of Factorial Zeroes Function
# https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/

# @param {Integer} k
# @return {Integer}
def preimage_size_fzf(k)
  zeros = lambda do |x|
    count = 0
    while x.positive?
      x /= 5
      count += x
    end
    count
  end

  first_ge = lambda do |target|
    lo = 0
    hi = 5 * (target + 1)
    while lo < hi
      mid = (lo + hi) / 2
      if zeros.call(mid) < target
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end

  zeros.call(first_ge.call(k)) == k ? 5 : 0
end
