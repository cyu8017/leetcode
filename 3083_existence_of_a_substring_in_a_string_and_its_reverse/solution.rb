# LeetCode 3083 - Existence of a Substring in a String and Its Reverse
# https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/

# @param {String} s
# @return {Boolean}
def is_substring_present(s)
  st = Array.new(26) { Array.new(26, false) }
  (0...s.length - 1).each do |i|
    st[s[i + 1].ord - 97][s[i].ord - 97] = true
  end
  (0...s.length - 1).each do |i|
    return true if st[s[i].ord - 97][s[i + 1].ord - 97]
  end
  false
end
