# LeetCode 2822 - Inversion of Object
# https://leetcode.com/problems/inversion-of-object/

# @param {Object} obj
# @return {Hash}
def invert_object(obj)
  inverted = {}
  keys = obj.is_a?(Hash) ? obj.keys : (0...obj.length)
  keys.each do |key|
    val = obj[key]
    key_s = key.to_s
    if inverted.key?(val)
      inverted[val] = [inverted[val]] unless inverted[val].is_a?(Array)
      inverted[val] << key_s
    else
      inverted[val] = key_s
    end
  end
  inverted
end
