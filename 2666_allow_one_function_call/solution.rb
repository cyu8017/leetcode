# LeetCode 2666 - Allow One Function Call
# https://leetcode.com/problems/allow-one-function-call/

# @param {Proc} fn
# @return {Proc}
def once(fn)
  called = false
  res = nil
  lambda do |*args|
    return nil if called

    called = true
    res = fn.call(*args)
    res
  end
end
