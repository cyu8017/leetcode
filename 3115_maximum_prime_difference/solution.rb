# LeetCode 3115 - Maximum Prime Difference
# https://leetcode.com/problems/maximum-prime-difference/

# @param {Integer[]} nums
# @return {Integer}
def maximum_prime_difference(nums)
  is_prime = lambda do |n|
    return false if n < 2
    i = 2
    while i * i <= n
      return false if n % i == 0
      i += 1
    end
    true
  end

  i = 0
  loop do
    if is_prime.call(nums[i])
      j = nums.length - 1
      loop do
        return j - i if is_prime.call(nums[j])
        j -= 1
      end
    end
    i += 1
  end
end
