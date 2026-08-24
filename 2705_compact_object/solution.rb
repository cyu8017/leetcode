# LeetCode 2705 - Compact Object
# https://leetcode.com/problems/compact-object/

# @param {Object} obj
# @return {Object}
def compact_object(obj)
  if obj.is_a?(Array)
    out = []
    obj.each do |x|
      v = compact_object(x)
      out << v if v
    end
    return out
  end
  if obj.is_a?(Hash)
    out = {}
    obj.each do |k, val|
      v = compact_object(val)
      out[k] = v if v
    end
    return out
  end
  obj
end
