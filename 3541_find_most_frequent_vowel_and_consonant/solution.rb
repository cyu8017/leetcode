# LeetCode 3541 - Find Most Frequent Vowel and Consonant
# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/

# @param {String} s
# @return {Integer}
def max_freq_sum(s)
  cnt = Array.new(26, 0)
  s.each_char { |c| cnt[c.ord - 97] += 1 }
  a = 0
  b = 0
  (0...26).each do |i|
    c = (97 + i).chr
    if "aeiou".include?(c)
      a = [a, cnt[i]].max
    else
      b = [b, cnt[i]].max
    end
  end
  a + b
end
