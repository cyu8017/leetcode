# LeetCode 3591 - Check if Any Element Has Prime Frequency
# https://leetcode.com/problems/check-if-any-element-has-prime-frequency/

# @param {Integer[]} nums
# @return {Boolean}
def check_prime_frequency(nums)
  is_prime = lambda do |x|
    return false if x < 2
    i = 2
    while i * i <= x
      return false if x % i == 0
      i += 1
    end
    true
  end
  cnt = {}
  nums.each { |x| cnt[x] = (cnt[x] || 0) + 1 }
  cnt.each_value { |v| return true if is_prime.call(v) }
  false
end
