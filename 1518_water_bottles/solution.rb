# LeetCode 1518 - Water Bottles
# https://leetcode.com/problems/water-bottles/

# @param {Integer} num_bottles
# @param {Integer} num_exchange
# @return {Integer}
def num_water_bottles(num_bottles, num_exchange)
  total = num_bottles
  while num_bottles >= num_exchange
    new_bottles = num_bottles / num_exchange
    remainder = num_bottles % num_exchange
    total += new_bottles
    num_bottles = new_bottles + remainder
  end
  total
end
