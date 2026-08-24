# LeetCode 0642 - Design Search Autocomplete System
# https://leetcode.com/problems/design-search-autocomplete-system/

class AutocompleteSystem
  def initialize(sentences, times)
    @counts = Hash.new(0)
    sentences.zip(times).each do |sentence, count|
      @counts[sentence] += count
    end
    @current = ""
  end

  def input(c)
    if c == "#"
      @counts[@current] += 1
      @current = ""
      return []
    end

    @current += c
    matches = @counts.keys.select { |sentence| sentence.start_with?(@current) }
    matches.sort_by! { |s| [-@counts[s], s] }
    matches.take(3)
  end
end
