# LeetCode 3324 - Find the Sequence of Strings Appeared on the Screen
# https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/

# @param {String} target
# @return {String[]}
def string_sequence(target)
  ans = []
  cur = ""
  target.each_char do |ch|
    cur += "a"
    ans << cur
    while cur[-1] != ch
      last = (cur[-1].ord + 1).chr
      cur = cur[0...-1] + last
      ans << cur
    end
  end
  ans
end
