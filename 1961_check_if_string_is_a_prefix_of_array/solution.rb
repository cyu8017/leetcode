# LeetCode 1961 - Check If String Is a Prefix of Array
# https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

# @param {String} s
# @param {String[]} words
# @return {Boolean}
def is_prefix_string(s, words)
  built = []
  words.each do |w|
    built << w
    cur = built.join
    return true if cur == s
    return false if cur.length > s.length || !s.start_with?(cur)
  end
  false
end
