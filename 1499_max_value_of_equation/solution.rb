# LeetCode 1499 - Max Value Of Equation
# https://leetcode.com/problems/max-value-of-equation/

def find_max_value_of_equation(points, k)
  q = []
  ans = -10**20
  points.each do |x, y|
    q.shift while !q.empty? && x - q[0][0] > k
    ans = [ans, x + y + q[0][1]].max unless q.empty?
    value = y - x
    q.pop while !q.empty? && q[-1][1] <= value
    q << [x, value]
  end
  ans
end
