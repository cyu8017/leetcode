# LeetCode 3314 - Construct the Minimum Bitwise Array I
# https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

# @param {Integer[]} nums
# @return {Integer[]}
def min_bitwise_array(nums)
  ans = Array.new(nums.length, -1)
  nums.each_with_index do |n, i|
    n.times do |x|
      if (x | (x + 1)) == n
        ans[i] = x
        break
      end
    end
  end
  ans
end
