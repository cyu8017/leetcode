# LeetCode 2342 - Max Sum of a Pair With Equal Sum of Digits
# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

# @param {Integer[]} nums
# @return {Integer}
def maximum_sum(nums)
  digit_sum = lambda do |x|
    s = 0
    while x > 0
      s += x % 10
      x /= 10
    end
    s
  end
  best = {}
  ans = -1
  nums.each do |x|
    ds = digit_sum.call(x)
    if best.key?(ds)
      cand = best[ds] + x
      ans = cand if cand > ans
      best[ds] = x if x > best[ds]
    else
      best[ds] = x
    end
  end
  ans
end
