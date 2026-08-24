# LeetCode 2618 - Check if Object Instance of Class
# https://leetcode.com/problems/check-if-object-instance-of-class/

# @param {Object} obj
# @param {Object} class_function
# @return {Boolean}
def check_if_instance_of(obj, class_function)
  return false if obj.nil?
  return false unless class_function.is_a?(Class)

  obj.is_a?(class_function)
rescue TypeError
  false
end
