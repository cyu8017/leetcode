# LeetCode 2754 - Bind Function to Context
# https://leetcode.com/problems/bind-function-to-context/

# @param {Proc} fn
# @param {Object} obj
# @return {Proc}
def bind_polyfill(fn, obj)
  lambda do |*args|
    if fn.respond_to?(:call)
      fn.call(*args)
    else
      fn
    end
  end
end
