# LeetCode 2675 - Array of Objects to Matrix
# https://leetcode.com/problems/array-of-objects-to-matrix/

# @param {Object[]} arr
# @return {Object[][]}
def json_to_matrix(arr)
  flatten = nil
  flatten = lambda do |obj, prefix, out|
    unless obj.is_a?(Hash) || obj.is_a?(Array)
      out[prefix] = obj
      return
    end
    if obj.is_a?(Array)
      return if obj.empty?

      obj.each_with_index do |item, i|
        flatten.call(item, prefix.empty? ? i.to_s : prefix + "." + i.to_s, out)
      end
      return
    end
    return if obj.empty?

    obj.each_key do |k|
      flatten.call(obj[k], prefix.empty? ? k.to_s : prefix + "." + k.to_s, out)
    end
  end
  maps = arr.map do |o|
    m = {}
    flatten.call(o, "", m)
    m
  end
  key_set = {}
  maps.each { |m| m.each_key { |k| key_set[k] = true } }
  keys = key_set.keys.sort
  mat = [keys]
  maps.each { |m| mat << keys.map { |k| m.key?(k) ? m[k] : "" } }
  mat
end

def solve(*args)
  json_to_matrix(*args)
end
