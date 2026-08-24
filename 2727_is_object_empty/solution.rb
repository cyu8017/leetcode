# LeetCode 2727 - Is Object Empty
# https://leetcode.com/problems/is-object-empty/

# @param {Object} obj
# @return {Boolean}
def is_empty(obj)
  obj.respond_to?(:empty?) ? obj.empty? : obj.nil?
end
