# LeetCode 2781 - Length of the Longest Valid Substring
# https://leetcode.com/problems/length-of-the-longest-valid-substring/

# @param {String} word
# @param {String[]} forbidden
# @return {Integer}
def longest_valid_substring(word, forbidden)
  forbid = {}
  max_len = 0
  forbidden.each do |f|
    forbid[f] = true
    max_len = [max_len, f.length].max
  end
  ans = 0
  right = word.length - 1
  (word.length - 1).downto(0) do |left|
    (left..right).each do |k|
      break if k - left + 1 > max_len
      if forbid[word[left..k]]
        right = k - 1
        break
      end
    end
    ans = [ans, right - left + 1].max
  end
  ans
end
