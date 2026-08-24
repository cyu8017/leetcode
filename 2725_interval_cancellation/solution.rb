# LeetCode 2725 - Interval Cancellation
# https://leetcode.com/problems/interval-cancellation/

# @param {Proc} fn
# @param {Object[]} args
# @param {Integer} t
# @return {Proc}
def cancellable(fn, args, t)
  cancelled = false
  fn.call(*args)
  Thread.new do
    until cancelled
      sleep(t / 1000.0)
      fn.call(*args) unless cancelled
    end
  end
  lambda { cancelled = true }
end
