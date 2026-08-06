# LeetCode 1100 - Find K-Length Substrings With No Repeated Characters
# https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def num_k_len_substr_no_repeats(s, k)
  return 0 if k > s.length
  window = Hash.new(0)
  s[0...k].each_char { |ch| window[ch] += 1 }
  ans = window.size == k ? 1 : 0
  (k...s.length).each do |i|
    window[s[i]] += 1
    left = s[i - k]
    window[left] -= 1
    window.delete(left) if window[left] == 0
    ans += 1 if window.size == k
  end
  ans
end
