# LeetCode 3233 - Find the Count of Numbers Which Are Not Special
# https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/

# @param {Integer} l
# @param {Integer} r
# @return {Integer}
def non_special_count(l, r)
  m = 31623
  primes = Array.new(m + 1, true)
  primes[0] = primes[1] = false
  (2..m).each do |i|
    next unless primes[i]
    (i * 2).step(m, i) { |j| primes[j] = false }
  end
  lo = Math.sqrt(l).ceil
  hi = Math.sqrt(r).floor
  cnt = 0
  (lo..hi).each { |i| cnt += 1 if primes[i] }
  r - l + 1 - cnt
end
