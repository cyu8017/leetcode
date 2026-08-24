# LeetCode 2434 - Using a Robot to Print the Lexicographically Smallest String
# https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

# @param {String} s
# @return {String}
def robot_with_string(s)
  n = s.length
  min_suf = Array.new(n + 1, "")
  min_suf[n] = ("z".ord + 1).chr
  (n - 1).downto(0) do |i|
    min_suf[i] = s[i] < min_suf[i + 1] ? s[i] : min_suf[i + 1]
  end
  stack = []
  ans = []
  (0...n).each do |i|
    stack << s[i]
    ans << stack.pop while !stack.empty? && stack[-1] <= min_suf[i + 1]
  end
  ans << stack.pop until stack.empty?
  ans.join
end
