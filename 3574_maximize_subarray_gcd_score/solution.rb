# LeetCode 3574 - Maximize Subarray GCD Score
# https://leetcode.com/problems/maximize-subarray-gcd-score/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_gcd_score(nums, k)
  gcd = lambda do |a, b|
    a, b = b, a % b while b != 0
    a
  end
  n = nums.length
  cnt = Array.new(n, 0)
  (0...n).each do |i|
    x = nums[i]
    while x.even?
      cnt[i] += 1
      x /= 2
    end
  end
  ans = 0
  (0...n).each do |l|
    g = 0
    mi = 2147483647
    t = 0
    (l...n).each do |r|
      g = gcd.call(g, nums[r])
      if cnt[r] < mi
        mi = cnt[r]
        t = 1
      elsif cnt[r] == mi
        t += 1
      end
      score = g * (r - l + 1)
      score *= 2 if t <= k
      ans = [ans, score].max
    end
  end
  ans
end
