# LeetCode 2224 - Minimum Number of Operations to Convert Time
# https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/

# @param {String} current
# @param {String} correct
# @return {Integer}
def convert_time(current, correct)
  to_min = lambda do |t|
    (t[0].ord - 48) * 600 + (t[1].ord - 48) * 60 + (t[3].ord - 48) * 10 + (t[4].ord - 48)
  end
  diff = to_min.call(correct) - to_min.call(current)
  ans = 0
  [60, 15, 5, 1].each do |step|
    ans += diff / step
    diff %= step
  end
  ans
end
