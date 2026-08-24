# LeetCode 0758 - Bold Words in String
# https://leetcode.com/problems/bold-words-in-string/

# @param {String[]} words
# @param {String} s
# @return {String}
def bold_words(words, s)
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
  parts.join.gsub("<b>", "**").gsub("</b>", "**")
end
