# LeetCode 2273 - Find Resultant Array After Removing Anagrams
# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

# @param {String[]} words
# @return {String[]}
def remove_anagrams(words)
  sig = lambda do |w|
    c = Array.new(26, 0)
    w.each_char { |ch| c[ch.ord - 97] += 1 }
    c
  end
  ans = [words[0]]
  prev = sig.call(words[0])
  (1...words.length).each do |i|
    cur = sig.call(words[i])
    unless cur == prev
      ans << words[i]
      prev = cur
    end
  end
  ans
end
