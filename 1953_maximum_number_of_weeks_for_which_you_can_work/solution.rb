# LeetCode 1953 - Maximum Number of Weeks for Which You Can Work
# https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/

# @param {Integer[]} milestones
# @return {Integer}
def number_of_weeks(milestones)
  total = milestones.sum
  mx = milestones.max
  rest = total - mx
  return 2 * rest + 1 if mx > rest + 1
  total
end
