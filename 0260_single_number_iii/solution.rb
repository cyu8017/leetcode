# LeetCode 0260 - Single Number III
# https://leetcode.com/problems/single-number-iii/

# @param {Integer[]} nums
# @return {Integer[]}
def single_number(nums)
  xor_all = nums.reduce(0, :^)
  diff = xor_all & -xor_all
  first = 0
  second = 0
  nums.each do |num|
    if num & diff != 0
      first ^= num
    else
      second ^= num
    end
  end
  [first, second]
end
