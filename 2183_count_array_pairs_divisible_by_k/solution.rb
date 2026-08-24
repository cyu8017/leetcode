# LeetCode 2183 - Count Array Pairs Divisible by K
# https://leetcode.com/problems/count-array-pairs-divisible-by-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_pairs(nums, k)
  gcd = lambda do |a, b|
    while b != 0
      a, b = b, a % b
    end
    a
  end

  freq = Hash.new(0)
  ans = 0
  nums.each do |x|
    g1 = gcd.call(x, k)
    freq.each { |g2, cnt| ans += cnt if (g1 * g2) % k == 0 }
    freq[g1] += 1
  end
  ans
end
