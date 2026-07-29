# LeetCode 1018 - Binary Prefix Divisible By 5
# https://leetcode.com/problems/binary-prefix-divisible-by-5/

# @param {Integer[]} nums
# @return {Boolean[]}
def prefixes_div_by5(nums)
  rem = 0
  nums.map do |bit|
    rem = (rem * 2 + bit) % 5
    rem.zero?
  end
end
