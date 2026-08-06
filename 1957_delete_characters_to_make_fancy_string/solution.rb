# LeetCode 1957 - Delete Characters to Make Fancy String
# https://leetcode.com/problems/delete-characters-to-make-fancy-string/

# @param {String} s
# @return {String}
def make_fancy_string(s)
  ans = []
  s.each_char do |c|
    next if ans.length >= 2 && ans[-1] == c && ans[-2] == c
    ans << c
  end
  ans.join
end
