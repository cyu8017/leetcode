# LeetCode 0961 - N-Repeated Element in Size 2N Array
# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

# @param {Integer[]} nums
# @return {Integer}
def repeated_n_times(nums)
  seen = {}
  nums.each do |x|
    return x if seen[x]

    seen[x] = true
  end
  -1
end
