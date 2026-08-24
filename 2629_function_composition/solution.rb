# LeetCode 2629 - Function Composition
# https://leetcode.com/problems/function-composition/

# @param {Proc[]} functions
# @return {Proc}
def compose(functions)
  lambda do |x|
    (functions.length - 1).downto(0) { |i| x = functions[i].call(x) }
    x
  end
end
