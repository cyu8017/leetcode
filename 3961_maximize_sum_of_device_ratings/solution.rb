# LeetCode 3961 - Maximize Sum Of Device Ratings
# https://leetcode.com/problems/maximize-sum-of-device-ratings/

# @param {Integer[][]} units
# @return {Integer}
def max_ratings(units)
  n = units[0].length
  if n == 1
    ans = 0
    units.each { |x| ans += x[0] }
    return ans
  end
  answer = 0
  mn = 2_147_483_647
  mn2 = 2_147_483_647
  units.each do |x|
    x = x.sort
    answer += x[1]
    mn2 = x[1] if x[1] < mn2
    mn = x[0] if x[0] < mn
  end
  answer - (mn2 - mn)
end
