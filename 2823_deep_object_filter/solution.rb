# LeetCode 2823 - Deep Object Filter
# https://leetcode.com/problems/deep-object-filter/

# @param {Object} obj
# @param {Proc} fn
# @return {Object}
def deep_filter(obj, fn)
  unless obj.is_a?(Hash) || obj.is_a?(Array)
    return fn.call(obj) ? obj : nil
  end
  if obj.is_a?(Array)
    res = []
    obj.each do |v|
      f = deep_filter(v, fn)
      res << f unless f.nil?
    end
    return res.empty? ? nil : res
  end
  res = {}
  obj.each do |k, v|
    f = deep_filter(v, fn)
    res[k] = f unless f.nil?
  end
  res.empty? ? nil : res
end
