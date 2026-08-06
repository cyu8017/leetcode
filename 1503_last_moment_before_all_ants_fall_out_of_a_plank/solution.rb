# LeetCode 1503 - Last Moment Before All Ants Fall Out of a Plank
# https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/

# @param {Integer} n
# @param {Integer[]} left
# @param {Integer[]} right
# @return {Integer}
def get_last_moment(n, left, right)
  left_max = left.empty? ? 0 : left.max
  right_min = right.empty? ? n : right.min
  [left_max, n - right_min].max
end
