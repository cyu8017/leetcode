# LeetCode 3805 - Count Caesar Cipher Pairs
# https://leetcode.com/problems/count-caesar-cipher-pairs/

# @param {String[]} words
# @return {Integer}
def count_pairs(words)
  cnt = Hash.new(0)
  words.each do |word|
    s = word.chars
    k = "z".ord - s[0].ord
    (1...s.length).each { |i| s[i] = (97 + (s[i].ord - 97 + k) % 26).chr }
    s[0] = "z"
    cnt[s.join] += 1
  end
  ans = 0
  cnt.each_value { |v| ans += v * (v - 1) / 2 }
  ans
end
