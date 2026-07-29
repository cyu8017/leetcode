# LeetCode 1087 - Brace Expansion
# https://leetcode.com/problems/brace-expansion/

# @param {String} s
# @return {String[]}
def expand(s)
  groups = []
  i = 0
  while i < s.length
    if s[i] == "{"
      j = s.index("}", i)
      groups << s[(i + 1)...j].split(",").sort
      i = j + 1
    else
      groups << [s[i]]
      i += 1
    end
  end
  ans = [""]
  groups.each do |group|
    ans = ans.flat_map { |prefix| group.map { |ch| prefix + ch } }
  end
  ans
end
