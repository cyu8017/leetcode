# LeetCode 3315 - Construct the Minimum Bitwise Array II
# https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/

# @param {Integer[]} nums
# @return {Integer[]}
def min_bitwise_array(nums)
  ans = Array.new(nums.length, -1)
  nums.each_with_index do |n, i|
    next if n == 2

    31.times do |b|
      next if ((n >> b) & 1) == 0

      x = n ^ (1 << b)
      if (x | (x + 1)) == n
        ans[i] = x
        break
      end
    end
  end
  ans
end
