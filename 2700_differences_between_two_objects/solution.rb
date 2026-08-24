# LeetCode 2700 - Differences Between Two Objects
# https://leetcode.com/problems/differences-between-two-objects/

# @param {Object} obj1
# @param {Object} obj2
# @return {Object}
def obj_diff(obj1, obj2)
  diff = {}
  keys = if obj1.is_a?(Hash)
           obj1.keys
         else
           obj1.is_a?(Array) ? (0...obj1.length).to_a : []
         end
  keys.each do |k|
    if obj1.is_a?(Hash)
      next unless obj2.is_a?(Hash) && obj2.key?(k)

      v1 = obj1[k]
      v2 = obj2[k]
    else
      next unless obj2.is_a?(Array) && k < obj2.length

      v1 = obj1[k]
      v2 = obj2[k]
    end
    if v1.is_a?(Hash) && v2.is_a?(Hash)
      child = obj_diff(v1, v2)
      diff[k] = child unless child.empty?
    elsif v1.is_a?(Array) && v2.is_a?(Array)
      child = obj_diff(v1, v2)
      diff[k] = child unless child.empty?
    elsif v1 != v2
      diff[k] = [v1, v2]
    end
  end
  diff
end

def solve(*args)
  obj_diff(*args)
end
