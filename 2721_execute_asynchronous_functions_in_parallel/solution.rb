# LeetCode 2721 - Execute Asynchronous Functions in Parallel
# https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/

# @param {Proc[]} functions
# @return {Array}
def promise_all(functions)
  n = functions.length
  return [] if n == 0

  ans = Array.new(n)
  n.times do |i|
    result = functions[i].call
    ans[i] = result.respond_to?(:call) ? result.call : result
  end
  ans
end
