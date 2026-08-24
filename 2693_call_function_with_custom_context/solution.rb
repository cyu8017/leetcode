# LeetCode 2693 - Call Function with Custom Context
# https://leetcode.com/problems/call-function-with-custom-context/

# @param {Proc} fn
# @param {Object} obj
# @return {Object}
def call_polyfill(fn, obj, *args)
  if obj.is_a?(Hash)
    key = Object.new
    obj[key] = fn
    res = obj[key].call(*args)
    obj.delete(key)
    return res
  end
  obj.define_singleton_method(:_call_polyfill_fn) { |*a| fn.call(*a) }
  res = obj._call_polyfill_fn(*args)
  res
end

def solve(*args)
  call_polyfill(*args)
end
