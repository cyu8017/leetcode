# LeetCode 2683 - Neighboring Bitwise XOR
# https://leetcode.com/problems/neighboring-bitwise-xor/

# @param {Integer[]} derived
# @return {Boolean}
def does_valid_array_exist(derived)
  x = 0
  derived.each { |v| x ^= v }
  x == 0
end
