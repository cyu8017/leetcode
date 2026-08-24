# LeetCode 2423 - Remove Letter To Equalize Frequency
# https://leetcode.com/problems/remove-letter-to-equalize-frequency/

# @param {String} word
# @return {Boolean}
def equal_frequency(word)
  (0...word.length).each do |skip|
    cnt = Array.new(26, 0)
    word.each_char.with_index do |ch, i|
      next if i == skip

      cnt[ch.ord - 97] += 1
    end
    freq = Hash.new(0)
    cnt.each { |c| freq[c] += 1 if c > 0 }
    return true if freq.length == 1
  end
  false
end
