# LeetCode 1402 - Reducing Dishes
# https://leetcode.com/problems/reducing-dishes/

def max_satisfaction(satisfaction)
  total = answer = 0
  satisfaction.sort.reverse_each do |value|
    break if total + value <= 0
    total += value
    answer += total
  end
  answer
end
