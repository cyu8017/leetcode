require "set"

class Solution
  def word_break(s, word_dict)
    words = word_dict.to_set
    memo = {}

    dfs = lambda do |start|
      return [""] if start == s.length
      return memo[start] if memo.key?(start)

      sentences = []
      ((start + 1)..s.length).each do |finish|
        word = s[start...finish]
        next unless words.include?(word)

        dfs.call(finish).each do |tail|
          sentences << (tail.empty? ? word : "#{word} #{tail}")
        end
      end
      memo[start] = sentences
    end

    dfs.call(0)
  end
end