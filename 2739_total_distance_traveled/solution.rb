# LeetCode 2739 - Total Distance Traveled
# https://leetcode.com/problems/total-distance-traveled/

# @param {Integer} main_tank
# @param {Integer} additional_tank
# @return {Integer}
def distance_traveled(main_tank, additional_tank)
  ans = 0
  while main_tank > 0
    if main_tank >= 5
      ans += 50
      main_tank -= 5
      if additional_tank > 0
        additional_tank -= 1
        main_tank += 1
      end
    else
      ans += main_tank * 10
      main_tank = 0
    end
  end
  ans
end
