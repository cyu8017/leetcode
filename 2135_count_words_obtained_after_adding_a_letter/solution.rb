# LeetCode 2135 - Count Words Obtained After Adding a Letter
# https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/

# @param {String[]} start_words
# @param {String[]} target_words
# @return {Integer}
def word_count(start_words, target_words)
  mask = lambda do |w|
    m = 0
    w.each_byte { |b| m |= 1 << (b - 97) }
    m
  end

  have = {}
  start_words.each { |w| have[mask.call(w)] = true }
  ans = 0
  target_words.each do |w|
    m = mask.call(w)
    w.each_byte do |b|
      if have[m ^ (1 << (b - 97))]
        ans += 1
        break
      end
    end
  end
  ans
end
