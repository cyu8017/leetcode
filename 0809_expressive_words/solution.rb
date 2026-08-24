# LeetCode 0809 - Expressive Words
# https://leetcode.com/problems/expressive-words/

# @param {String} s
# @param {String[]} words
# @return {Integer}
def expressive_words(s, words)
  groups = lambda do |text|
    result = []
    i = 0
    while i < text.length
      j = i
      j += 1 while j < text.length && text[j] == text[i]
      result << [text[i], j - i]
      i = j
    end
    result
  end

  target = groups.call(s)
  words.count do |word|
    source = groups.call(word)
    next false if source.length != target.length

    source.zip(target).all? do |(ch1, c1), (ch2, c2)|
      ch1 == ch2 && c1 <= c2 && (c1 == c2 || c2 >= 3)
    end
  end
end
