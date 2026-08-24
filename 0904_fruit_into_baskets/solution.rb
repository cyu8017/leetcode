# LeetCode 0904 - Fruit Into Baskets
# https://leetcode.com/problems/fruit-into-baskets/

# @param {Integer[]} fruits
# @return {Integer}
def total_fruit(fruits)
  count = Hash.new(0)
  left = 0
  ans = 0
  fruits.each_with_index do |kind, right|
    count[kind] += 1
    while count.length > 2
      count[fruits[left]] -= 1
      count.delete(fruits[left]) if count[fruits[left]] == 0
      left += 1
    end
    ans = [ans, right - left + 1].max
  end
  ans
end
