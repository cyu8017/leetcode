
# @param {String} word
# @return {Integer}
def longest_beautiful_substring(word)
  vowels = 'aeiou'
  best = 0

  word.each_char.with_index do |ch, start|
    next unless ch == 'a'

    counts = Array.new(5, 0)
    (start...word.length).each do |endi|
      current = word[endi]
      break if endi > start && current < word[endi - 1]

      idx = vowels.index(current)
      break if idx.nil?
      counts[idx] += 1
      break if idx > 0 && counts[idx - 1] == 0
      best = [best, endi - start + 1].max if counts.all? { |c| c > 0 }
    end
  end
  best
end
