# LeetCode 2775 - Undefined to Null
# https://leetcode.com/problems/undefined-to-null/

# @param {Object} obj
# @return {Object}
def undefined_to_null(obj)
  if obj.is_a?(String) && obj.lstrip.start_with?("{", "[")
    require "json"
    obj = JSON.parse(obj.gsub(/\bundefined\b/, "null"))
  end
  return nil if obj.nil?
  return obj unless obj.is_a?(Hash) || obj.is_a?(Array)
  if obj.is_a?(Array)
    obj.each_index { |i| obj[i] = undefined_to_null(obj[i]) }
    return obj
  end
  obj.keys.each { |k| obj[k] = undefined_to_null(obj[k]) }
  obj
end
