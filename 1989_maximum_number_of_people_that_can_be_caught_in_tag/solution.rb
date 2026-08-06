# LeetCode 1989 - Maximum Number of People That Can Be Caught in Tag
# https://leetcode.com/problems/maximum-number-of-people-that-can-be-caught-in-tag/

# @param {Integer[]} team
# @param {Integer} dist
# @return {Integer}
def catch_maximum_amountof_people(team, dist)
  ans = j = 0
  n = team.length
  team.each_with_index do |x, i|
    next if x.zero?
    j += 1 while j < n && (team[j] == 1 || i - j > dist)
    if j < n && (i - j).abs <= dist
      ans += 1
      j += 1
    end
  end
  ans
end
