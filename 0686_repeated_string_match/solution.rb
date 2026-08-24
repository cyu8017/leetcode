# LeetCode 0686 - Repeated String Match
# https://leetcode.com/problems/repeated-string-match/

# @param {String} a
# @param {String} b
# @return {Integer}
def repeated_string_match(a, b)
  repeats = (b.length + a.length - 1) / a.length
  built = a * repeats
  return repeats if built.include?(b)
  return repeats + 1 if (built + a).include?(b)

  -1
end
