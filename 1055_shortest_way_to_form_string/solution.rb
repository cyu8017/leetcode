# LeetCode 1055 - Shortest Way to Form String
# https://leetcode.com/problems/shortest-way-to-form-string/

# @param {String} source
# @param {String} target
# @return {Integer}
def shortest_way(source, target)
  source_chars = {}
  source.each_char { |ch| source_chars[ch] = true }
  return -1 if target.each_char.any? { |ch| !source_chars[ch] }

  ans = 0
  i = 0
  n = target.length
  while i < n
    ans += 1
    source.each_char do |ch|
      if i < n && target[i] == ch
        i += 1
      end
    end
  end
  ans
end
