require "set"

class Solution
  def word_break(s, word_dict)
    words = word_dict.to_set
    can_break = Array.new(s.length + 1, false)
    can_break[0] = true

    (1..s.length).each do |finish|
      (0...finish).each do |start|
        next unless can_break[start] && words.include?(s[start...finish])

        can_break[finish] = true
        break
      end
    end
    can_break[-1]
  end
end