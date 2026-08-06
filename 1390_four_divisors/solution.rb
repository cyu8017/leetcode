# LeetCode 1390 - Four Divisors
# https://leetcode.com/problems/four-divisors/

def sum_four_divisors(nums)
  ans = 0
  nums.each do |x|
    ds = {}
    (1..Math.sqrt(x).to_i).each do |d|
      next unless x % d == 0
      ds[d] = true
      ds[x / d] = true
      break if ds.length > 4
    end
    ans += ds.keys.sum if ds.length == 4
  end
  ans
end
