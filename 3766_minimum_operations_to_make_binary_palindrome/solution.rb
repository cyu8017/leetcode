# LeetCode 3766 - Minimum Operations to Make Binary Palindrome
# https://leetcode.com/problems/minimum-operations-to-make-binary-palindrome/

# @param {Integer[]} nums
# @return {Integer[]}
def min_operations(nums)
  pals = []
  nmax = 1 << 14
  is_palindrome = lambda do |s|
    m = s.length
    (0...(m / 2)).each { |i| return false if s[i] != s[m - 1 - i] }
    true
  end
  (0...nmax).each do |i|
    x = i
    if x == 0
      sb = "0"
    else
      bits = []
      while x > 0
        bits << (48 + (x & 1)).chr
        x >>= 1
      end
      sb = bits.reverse.join
    end
    pals << i if is_palindrome.call(sb)
  end
  lower_bound = lambda do |x|
    lo = 0
    hi = pals.length
    while lo < hi
      mid = (lo + hi) >> 1
      if pals[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
  ans = Array.new(nums.length, 0)
  nums.each_with_index do |x, k|
    it = lower_bound.call(x)
    t = 10**18
    t = pals[it] - x if it < pals.length
    t = [t, x - pals[it - 1]].min if it > 0
    ans[k] = t
  end
  ans
end
