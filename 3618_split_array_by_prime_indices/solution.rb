# LeetCode 3618 - Split Array by Prime Indices
# https://leetcode.com/problems/split-array-by-prime-indices/

# @param {Integer[]} nums
# @return {Integer}
def split_array(nums)
  pr = primes3618
  ans = 0
  nums.each_with_index do |x, i|
    ans += pr[i] ? x : -x
  end
  ans.abs
end

def primes3618
  return $primes3618 if defined?($primes3618) && $primes3618

  m = 100010
  primes = Array.new(m, true)
  primes[0] = primes[1] = false
  (2...m).each do |i|
    next unless primes[i]

    (i + i...m).step(i) { |j| primes[j] = false }
  end
  $primes3618 = primes
end
