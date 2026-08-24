# LeetCode 3589 - Count Prime-Gap Balanced Subarrays
# https://leetcode.com/problems/count-prime-gap-balanced-subarrays/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def prime_subarray(nums, k)
  mx = nums.max
  is_prime = Array.new(mx + 1, false)
  (2..mx).each { |i| is_prime[i] = true }
  i = 2
  while i * i <= mx
    if is_prime[i]
      (i * i).step(mx, i) { |j| is_prime[j] = false }
    end
    i += 1
  end
  n = nums.length
  ans = 0
  (0...n).each do |l|
    primes = []
    (l...n).each do |r|
      primes << nums[r] if is_prime[nums[r]]
      if primes.length >= 2
        mn = primes[0]
        mxp = primes[0]
        primes.each do |p|
          mn = [mn, p].min
          mxp = [mxp, p].max
        end
        ans += 1 if mxp - mn <= k
      end
    end
  end
  ans
end
