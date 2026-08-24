# LeetCode 3913 - Sort Vowels by Frequency
# https://leetcode.com/problems/sort-vowels-by-frequency/

# @param {String} s
# @return {String}
def sort_vowels(s)
  st = { "a" => true, "e" => true, "i" => true, "o" => true, "u" => true }
  vowels = []
  cnt = {}
  s.each_char do |c|
    next unless st[c]
    unless cnt.key?(c)
      vowels << c
      cnt[c] = 0
    end
    cnt[c] += 1
  end
  vowels.sort_by! { |ch| -cnt[ch] }
  ans = s.chars
  i = 0
  s.length.times do |k|
    next unless st[s[k]]
    ch = vowels[i]
    ans[k] = ch
    cnt[ch] -= 1
    i += 1 if cnt[ch] == 0
  end
  ans.join
end
