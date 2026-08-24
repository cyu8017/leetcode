# LeetCode 2623 - Memoize
# https://leetcode.com/problems/memoize/

# @param {Proc} fn
# @return {Proc}
def memoize(fn)
  cache = {}
  lambda do |x|
    return cache[x] if cache.key?(x)

    r = fn.call(x)
    cache[x] = r
    r
  end
end

def solve(*args)
  memoize(*args)
end
