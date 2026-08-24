# LeetCode 2232 - Minimize Result by Adding Parentheses to Expression
# https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/

# @param {String} expression
# @return {String}
def minimize_result(expression)
  plus = expression.index("+")
  left = expression[0...plus]
  right = expression[(plus + 1)..]
  best_val = Float::INFINITY
  best = ""
  (0...left.length).each do |i|
    (1..right.length).each do |j|
      a = left[0...i]
      b = left[i..]
      c = right[0...j]
      d = right[j..]
      val = b.to_i + c.to_i
      val *= a.to_i unless a.empty?
      val *= d.to_i unless d.empty?
      if val < best_val
        best_val = val
        best = "#{a}(#{b}+#{c})#{d}"
      end
    end
  end
  best
end
