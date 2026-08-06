# LeetCode 1455 - Check If A Word Occurs As A Prefix Of Any Word In A Sentence
# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

def is_prefix_of_word(sentence, search_word)
  sentence.split.each_with_index do |w, i|
    return i + 1 if w.start_with?(search_word)
  end
  -1
end
