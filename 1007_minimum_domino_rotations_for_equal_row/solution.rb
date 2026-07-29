# LeetCode 1007 - Minimum Domino Rotations For Equal Row
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

# @param {Integer[]} tops
# @param {Integer[]} bottoms
# @return {Integer}
def min_domino_rotations(tops, bottoms)
  check = lambda do |target|
    rot_top = rot_bot = 0
    tops.zip(bottoms).each do |t, b|
      return Float::INFINITY if t != target && b != target

      rot_top += 1 if t != target
      rot_bot += 1 if b != target
    end
    [rot_top, rot_bot].min
  end
  ans = [check.call(tops[0]), check.call(bottoms[0])].min
  ans == Float::INFINITY ? -1 : ans
end
