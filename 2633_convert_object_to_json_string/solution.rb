# LeetCode 2633 - Convert Object to JSON String
# https://leetcode.com/problems/convert-object-to-json-string/

# @param {Object} object
# @return {String}
def json_stringify(object)
  return "null" if object.nil?
  return '"' + object + '"' if object.is_a?(String)
  return object ? "true" : "false" if object == true || object == false
  return object.to_s if object.is_a?(Integer) || object.is_a?(Float)
  return "[" + object.map { |x| json_stringify(x) }.join(",") + "]" if object.is_a?(Array)

  "{" + object.keys.map { |k| '"' + k.to_s + '":' + json_stringify(object[k]) }.join(",") + "}"
end

def solve(*args)
  json_stringify(*args)
end
