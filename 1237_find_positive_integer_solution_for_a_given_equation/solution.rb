# LeetCode 1237 - Find Positive Integer Solution for a Given Equation
# https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

# @param {CustomFunction} customfunction
# @param {Integer} z
# @return {Integer[][]}
def find_solution(customfunction, z)
  answer = []
  x = 1
  y = 1000
  while x <= 1000 && y >= 1
    value = customfunction.f(x, y)
    if value == z
      answer << [x, y]
      x += 1
      y -= 1
    elsif value < z
      x += 1
    else
      y -= 1
    end
  end
  answer
end
