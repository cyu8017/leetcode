# LeetCode 3775 - Reverse Words with Same Vowel Count
# https://leetcode.com/problems/reverse-words-with-same-vowel-count/

# @param {String} s
# @return {String}
def reverse_words(s)
  calc = lambda do |w|
    cnt = 0
    w.each_char { |c| cnt += 1 if "aeiou".include?(c) }
    cnt
  end
  words = s.strip.split
  cnt = calc.call(words[0])
  ans = words[0]
  (1...words.length).each do |i|
    w = words[i]
    w = w.reverse if calc.call(w) == cnt
    ans += " " + w
  end
  ans
end
