# LeetCode 2815 - Max Pair Sum in an Array
# https://leetcode.com/problems/max-pair-sum-in-an-array/

# @param {Integer[]} nums
# @return {Integer}
def max_sum(nums)
  best = {}
  ans = -1
  nums.each do |v|
    x = v
    md = 0
    while x > 0
      md = [md, x % 10].max
      x /= 10
    end
    if best.key?(md)
      ans = [ans, best[md] + v].max
      best[md] = [best[md], v].max
    else
      best[md] = v
    end
  end
  ans
end
