# LeetCode 3085 - Minimum Deletions to Make String K-Special
# https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/

# @param {String} word
# @param {Integer} k
# @return {Integer}
def minimum_deletions(word, k)
  freq = Array.new(26, 0)
  word.each_char { |ch| freq[ch.ord - 97] += 1 }
  nums = freq.select { |v| v > 0 }
  ans = word.length
  (0..word.length).each do |i|
    cur = 0
    nums.each do |x|
      if x < i
        cur += x
      elsif x > i + k
        cur += x - i - k
      end
    end
    ans = [ans, cur].min
  end
  ans
end
