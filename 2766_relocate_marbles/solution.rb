# LeetCode 2766 - Relocate Marbles
# https://leetcode.com/problems/relocate-marbles/

# @param {Integer[]} nums
# @param {Integer[]} move_from
# @param {Integer[]} move_to
# @return {Integer[]}
def relocate_marbles(nums, move_from, move_to)
  pos = {}
  nums.each { |v| pos[v] = true }
  move_from.each_with_index do |src, i|
    pos.delete(src)
    pos[move_to[i]] = true
  end
  pos.keys.sort
end
