# LeetCode 2636 - Promise Pool
# https://leetcode.com/problems/promise-pool/

# @param {Proc[]} functions
# @param {Integer} n
# @return {NilClass}
def promise_pool(functions, n = 1)
  i = 0
  worker = lambda do
    while i < functions.length
      cur = i
      i += 1
      functions[cur].call
    end
  end
  [n, functions.length].min.times { worker.call }
  nil
end

def solve(*args)
  promise_pool(*args)
end
