# LeetCode 0575 - Distribute Candies
# https://leetcode.com/problems/distribute-candies/

# @param {Integer[]} candy_type
# @return {Integer}
def distribute_candies(candy_type)
  [candy_type.uniq.length, candy_type.length / 2].min
end
