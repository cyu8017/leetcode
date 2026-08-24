# LeetCode 3481 - Apply Substitutions
# https://leetcode.com/problems/apply-substitutions/

# @param {String[][]} replacements
# @param {String} text
# @return {String}
def apply_substitutions(replacements, text)
  mp = {}
  replacements.each { |r| mp[r[0]] = r[1] }
  resolve = nil
  resolve = lambda do |s|
    out = []
    i = 0
    while i < s.length
      if s[i] == "%"
        j = i + 1
        j += 1 while j < s.length && s[j] != "%"
        key = s[(i + 1)...j]
        out << resolve.call(mp[key])
        i = j + 1
      else
        out << s[i]
        i += 1
      end
    end
    out.join
  end
  resolve.call(text)
end
