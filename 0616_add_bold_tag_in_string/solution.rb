# LeetCode 0616 - Add Bold Tag in String
# https://leetcode.com/problems/add-bold-tag-in-string/

# @param {String} s
# @param {String[]} words
# @return {String}
def add_bold_tag(s, words)
  n = s.length
  bold = Array.new(n, false)

  words.each do |word|
    start = s.index(word)
    while start
      (start...(start + word.length)).each { |i| bold[i] = true }
      start = s.index(word, start + 1)
    end
  end

  parts = []
  i = 0
  while i < n
    if bold[i]
      parts << "<b>"
      while i < n && bold[i]
        parts << s[i]
        i += 1
      end
      parts << "</b>"
    else
      parts << s[i]
      i += 1
    end
  end

  parts.join
end
