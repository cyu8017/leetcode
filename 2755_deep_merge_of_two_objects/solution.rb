# LeetCode 2755 - Deep Merge of Two Objects
# https://leetcode.com/problems/deep-merge-of-two-objects/

# @param {Object} obj1
# @param {Object} obj2
# @return {Object}
def deep_merge(obj1, obj2)
  merge = lambda do |a, b|
    if a.is_a?(Hash) && b.is_a?(Hash)
      res = a.dup
      b.each do |k, v|
        res[k] = res.key?(k) ? merge.call(res[k], v) : v
      end
      res
    elsif a.is_a?(Array) && b.is_a?(Array)
      n = [a.length, b.length].max
      (0...n).map do |i|
        if i >= a.length
          b[i]
        elsif i >= b.length
          a[i]
        else
          merge.call(a[i], b[i])
        end
      end
    else
      b
    end
  end
  merge.call(obj1, obj2)
end
