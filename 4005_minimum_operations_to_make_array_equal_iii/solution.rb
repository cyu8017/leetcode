# LeetCode 4005 - Minimum Operations to Make Array Equal III
# https://leetcode.com/problems/minimum-operations-to-make-array-equal-iii/

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  cost = lambda do |x, t|
    return 0 if x == t
    return 1 if x % t == 0 || t % x == 0
    2
  end
  gcd = lambda do |a, b|
    while b != 0
      a, b = b, a % b
    end
    a
  end
  n = nums.length
  return 0 if n <= 1
  g = nums[0]
  mn = nums[0]
  (1...n).each do |i|
    g = gcd.call(g, nums[i])
    mn = nums[i] if nums[i] < mn
  end
  cands = {}
  nums.each { |x| cands[x] = true }
  d = 1
  while d * d <= mn
    if mn % d == 0
      cands[d] = true
      cands[mn / d] = true
    end
    d += 1
  end
  cands[g] = true
  ans = 2_147_483_647
  cands.keys.each do |t|
    s = 0
    nums.each do |x|
      s += cost.call(x, t)
      break if s >= ans
    end
    ans = s if s < ans
  end
  ans
end
