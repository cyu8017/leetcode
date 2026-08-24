# LeetCode 3846 - Total Distance to Type a String Using One Finger
# https://leetcode.com/problems/total-distance-to-type-a-string-using-one-finger/

POS_3846 = {}
KEYS_3846 = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
3.times do |i|
  KEYS_3846[i].length.times { |j| POS_3846[KEYS_3846[i][j]] = [i, j] }
end

# @param {String} s
# @return {Integer}
def total_distance(s)
  pre = "a"
  ans = 0
  s.each_char do |cur|
    p1 = POS_3846[pre]
    p2 = POS_3846[cur]
    ans += (p1[0] - p2[0]).abs + (p1[1] - p2[1]).abs
    pre = cur
  end
  ans
end
