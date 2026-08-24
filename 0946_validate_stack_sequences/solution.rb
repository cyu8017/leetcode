# LeetCode 0946 - Validate Stack Sequences
# https://leetcode.com/problems/validate-stack-sequences/

# @param {Integer[]} pushed
# @param {Integer[]} popped
# @return {Boolean}
def validate_stack_sequences(pushed, popped)
  stack = []
  j = 0
  pushed.each do |x|
    stack << x
    while !stack.empty? && stack[-1] == popped[j]
      stack.pop
      j += 1
    end
  end
  stack.empty?
end
