# LeetCode 2630 - Memoize II
# https://leetcode.com/problems/memoize-ii/

# @param {Proc} fn
# @return {Proc}
def memoize(fn)
  root = {}
  res_key = Object.new
  lambda do |*args|
    node = root
    args.each do |a|
      node[a] = {} unless node.key?(a)
      node = node[a]
    end
    return node[res_key] if node.key?(res_key)

    v = fn.call(*args)
    node[res_key] = v
    v
  end
end

def solve(*args)
  memoize(*args)
end
