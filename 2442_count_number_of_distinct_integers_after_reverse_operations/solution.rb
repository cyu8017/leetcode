# LeetCode 2442 - Count Number of Distinct Integers After Reverse Operations
# https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

# @param {Integer[]} nums
# @return {Integer}
def count_distinct_integers(nums)
  rev = lambda do |x|
    r = 0
    while x > 0
      r = r * 10 + x % 10
      x /= 10
    end
    r
  end

  seen = {}
  nums.each do |x|
    seen[x] = true
    seen[rev.call(x)] = true
  end
  seen.length
end
