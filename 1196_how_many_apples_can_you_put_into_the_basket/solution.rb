# LeetCode 1196 - How Many Apples Can You Put into the Basket
# https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/

# @param {Integer[]} weight
# @return {Integer}
def max_number_of_apples(weight)
  weight = weight.sort
  total = 0
  weight.each_with_index do |w, i|
    total += w
    return i if total > 5000
  end
  weight.length
end
