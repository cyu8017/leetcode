# LeetCode 2637 - Promise Time Limit
# https://leetcode.com/problems/promise-time-limit/

# @param {Proc} fn
# @param {Integer} t
# @return {Proc}
def time_limit(fn, t)
  lambda do |*args|
    start = Time.now
    res = fn.call(*args)
    raise "Time Limit Exceeded" if (Time.now - start) * 1000 > t

    res
  end
end
