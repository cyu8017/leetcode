# LeetCode 0833 - Find And Replace in String
# https://leetcode.com/problems/find-and-replace-in-string/

# @param {String} s
# @param {Integer[]} indices
# @param {String[]} sources
# @param {String[]} targets
# @return {String}
def find_replace_string(s, indices, sources, targets)
  replace = {}
  indices.zip(sources, targets).each do |i, src, tgt|
    replace[i] = [src.length, tgt] if s[i, src.length] == src
  end
  out = []
  i = 0
  while i < s.length
    if replace.key?(i)
      length, tgt = replace[i]
      out << tgt
      i += length
    else
      out << s[i]
      i += 1
    end
  end
  out.join
end
