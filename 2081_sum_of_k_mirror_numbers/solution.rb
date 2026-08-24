# LeetCode 2081 - Sum of k-Mirror Numbers
# https://leetcode.com/problems/sum-of-k-mirror-numbers/

# @param {Integer} k
# @param {Integer} n
# @return {Integer}
def k_mirror(k, n)
  is_pal_base = lambda do |x, bas|
    digits = []
    while x > 0
      digits << x % bas
      x /= bas
    end
    l = 0
    r = digits.length - 1
    while l < r
      return false if digits[l] != digits[r]

      l += 1
      r -= 1
    end
    true
  end

  ans = 0
  count = 0
  length = 1
  while count < n
    start = 1
    ((length + 1) / 2 - 1).times { start *= 10 }
    finish = start * 10
    half = start
    while half < finish && count < n
      pal = half
      if length.even?
        x = half
        while x > 0
          pal = pal * 10 + x % 10
          x /= 10
        end
      else
        x = half / 10
        while x > 0
          pal = pal * 10 + x % 10
          x /= 10
        end
      end
      if is_pal_base.call(pal, k)
        ans += pal
        count += 1
      end
      half += 1
    end
    length += 1
  end
  ans
end
