# LeetCode 2628 - JSON Deep Equal
# https://leetcode.com/problems/json-deep-equal/

# @param {Object} o1
# @param {Object} o2
# @return {Boolean}
def are_deeply_equal(o1, o2)
  return true if o1.equal?(o2)
  return false if o1.class != o2.class
  return false if o1.nil? || o2.nil?
  return o1 == o2 unless o1.is_a?(Array) || o1.is_a?(Hash)
  return false if o1.is_a?(Array) != o2.is_a?(Array)

  if o1.is_a?(Array)
    return false if o1.length != o2.length

    o1.each_index { |i| return false unless are_deeply_equal(o1[i], o2[i]) }
    return true
  end
  return false if o1.length != o2.length

  o1.each_key { |k| return false if !o2.key?(k) || !are_deeply_equal(o1[k], o2[k]) }
  true
end

def solve(*args)
  are_deeply_equal(*args)
end
