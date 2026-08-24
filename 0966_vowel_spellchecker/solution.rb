# LeetCode 0966 - Vowel Spellchecker
# https://leetcode.com/problems/vowel-spellchecker/

# @param {String[]} wordlist
# @param {String[]} queries
# @return {String[]}
def spellchecker(wordlist, queries)
  vowels = { "a" => true, "e" => true, "i" => true, "o" => true, "u" => true }
  devowel = lambda do |w|
    w.downcase.chars.map { |c| vowels[c] ? "*" : c }.join
  end
  exact = {}
  wordlist.each { |w| exact[w] = true }
  lower = {}
  vowel_map = {}
  wordlist.each do |w|
    low = w.downcase
    lower[low] = w unless lower.key?(low)
    key = devowel.call(w)
    vowel_map[key] = w unless vowel_map.key?(key)
  end

  queries.map do |q|
    if exact[q]
      q
    elsif lower.key?(q.downcase)
      lower[q.downcase]
    elsif vowel_map.key?(devowel.call(q))
      vowel_map[devowel.call(q)]
    else
      ""
    end
  end
end
