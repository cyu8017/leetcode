# LeetCode 1863 - Sum of All Subset XOR Totals
# https://leetcode.com/problems/sum-of-all-subset-xor-totals/

# @param {Integer[]} nums
# @return {Integer}
def subset_x_o_r_sum(nums)
  bits = 0
  nums.each { |num| bits |= num }

  total = 0
  bit = 1
  while bit <= bits
    total += bit if (bits & bit) != 0
    bit <<= 1
  end

  total << (nums.length - 1)
end
