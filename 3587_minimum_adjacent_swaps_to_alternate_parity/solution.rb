# LeetCode 3587 - Minimum Adjacent Swaps to Alternate Parity
# https://leetcode.com/problems/minimum-adjacent-swaps-to-alternate-parity/

# @param {Integer[]} nums
# @return {Integer}
def min_swaps(nums)
  calc = lambda do |pos, n, k|
    res = 0
    (0...n).step(2) { |i| res += (pos[k][i / 2] - i).abs }
    res
  end
  pos = [[], []]
  nums.each_with_index { |x, i| pos[x & 1] << i }
  return -1 if (pos[0].length - pos[1].length).abs > 1
  return calc.call(pos, nums.length, 0) if pos[0].length > pos[1].length
  return calc.call(pos, nums.length, 1) if pos[0].length < pos[1].length
  [calc.call(pos, nums.length, 0), calc.call(pos, nums.length, 1)].min
end
