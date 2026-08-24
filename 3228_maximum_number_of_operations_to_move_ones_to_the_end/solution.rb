# LeetCode 3228 - Maximum Number of Operations to Move Ones to the End
# https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/

# @param {String} s
# @return {Integer}
def max_operations(s)
  ans = 0
  cnt = 0
  s.each_char.with_index do |ch, i|
    if ch == "1"
      cnt += 1
    elsif i > 0 && s[i - 1] == "1"
      ans += cnt
    end
  end
  ans
end
