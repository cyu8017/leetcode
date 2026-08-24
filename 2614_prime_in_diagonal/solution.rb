# LeetCode 2614 - Prime In Diagonal
# https://leetcode.com/problems/prime-in-diagonal/

# @param {Integer[][]} nums
# @return {Integer}
def diagonal_prime(nums)
  is_prime = lambda do |x|
    return false if x < 2

    i = 2
    while i * i <= x
      return false if x % i == 0

      i += 1
    end
    true
  end

  n = nums.length
  best = 0
  n.times do |i|
    a = nums[i][i]
    b = nums[i][n - 1 - i]
    best = a if is_prime.call(a) && a > best
    best = b if is_prime.call(b) && b > best
  end
  best
end
