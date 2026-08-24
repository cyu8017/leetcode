# LeetCode 2469 - Convert the Temperature
# https://leetcode.com/problems/convert-the-temperature/

# @param {Float} celsius
# @return {Float[]}
def convert_temperature(celsius)
  [celsius + 273.15, celsius * 1.80 + 32.00]
end
