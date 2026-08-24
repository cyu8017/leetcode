# LeetCode 2631 - Group By
# https://leetcode.com/problems/group-by/

# @param {Object[]} array
# @param {Proc} fn
# @return {Hash}
def group_by(array, fn)
  out = {}
  array.each do |x|
    k = fn.call(x)
    out[k] ||= []
    out[k] << x
  end
  out
end

def solve(*args)
  group_by(*args)
end
