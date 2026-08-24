# LeetCode 3853 - Merge Close Characters
# https://leetcode.com/problems/merge-close-characters/

# @param {String} s
# @param {Integer} k
# @return {String}
def merge_characters(s, k)
  last = {}
  ans = ""
  s.each_char do |c|
    cur = ans.length
    next if last.key?(c) && cur - last[c] <= k
    ans += c
    last[c] = cur
  end
  ans
end
