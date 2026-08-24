# LeetCode 2715 - Timeout Cancellation
# https://leetcode.com/problems/timeout-cancellation/

# @param {Proc} fn
# @param {Object[]} args
# @param {Integer} t
# @return {Proc}
def cancellable(fn, args, t)
  cancelled = false
  Thread.new do
    sleep(t / 1000.0)
    fn.call(*args) unless cancelled
  end
  lambda { cancelled = true }
end
