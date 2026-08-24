# LeetCode 3079 - Find the Sum of Encrypted Integers
# https://leetcode.com/problems/find-the-sum-of-encrypted-integers/

# @param {Integer[]} nums
# @return {Integer}
def sum_of_encrypted_int(nums)
  encrypt = lambda do |x|
    mx = 0
    p = 0
    while x > 0
      mx = [mx, x % 10].max
      p = p * 10 + 1
      x /= 10
    end
    mx * p
  end
  nums.sum { |x| encrypt.call(x) }
end
