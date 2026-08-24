# LeetCode 2358 - Maximum Number of Groups Entering a Competition
# https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/

# @param {Integer[]} grades
# @return {Integer}
def maximum_groups(grades)
  n = grades.length
  k = 0
  k += 1 while (k + 1) * (k + 2) / 2 <= n
  k
end
