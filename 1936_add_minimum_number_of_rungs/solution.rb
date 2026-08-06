# LeetCode 1936 - Add Minimum Number of Rungs
# https://leetcode.com/problems/add-minimum-number-of-rungs/

# @param {Integer[]} rungs
# @param {Integer} dist
# @return {Integer}
def add_rungs(rungs, dist)
  prev = 0
  ans = 0
  rungs.each do |r|
    ans += (r - prev - 1) / dist
    prev = r
  end
  ans
end
