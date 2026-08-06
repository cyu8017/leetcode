# LeetCode 1593 - Split a String Into the Max Number of Unique Substrings
# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/

# @param {String} s
# @return {Integer}
def max_unique_split(s)
  used = {}
  answer = 0
  dfs = lambda do |i|
    return if used.length + s.length - i <= answer
    if i == s.length
      answer = [answer, used.length].max
      return
    end
    ((i + 1)..s.length).each do |j|
      part = s[i...j]
      next if used[part]
      used[part] = true
      dfs.call(j)
      used.delete(part)
    end
  end
  dfs.call(0)
  answer
end
