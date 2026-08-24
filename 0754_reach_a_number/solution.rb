# LeetCode 0754 - Reach a Number
# https://leetcode.com/problems/reach-a-number/

# @param {Integer} target
# @return {Integer}
def reach_number(target)
  target = target.abs
  steps = 0
  total = 0
  while total < target || (total - target).odd?
    steps += 1
    total += steps
  end
  steps
end
