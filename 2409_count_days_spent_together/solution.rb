# LeetCode 2409 - Count Days Spent Together
# https://leetcode.com/problems/count-days-spent-together/

# @param {String} arrive_alice
# @param {String} leave_alice
# @param {String} arrive_bob
# @param {String} leave_bob
# @return {Integer}
def count_days_together(arrive_alice, leave_alice, arrive_bob, leave_bob)
  days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  to_day = lambda do |s|
    m = (s[0].ord - 48) * 10 + (s[1].ord - 48)
    d = (s[3].ord - 48) * 10 + (s[4].ord - 48)
    res = d
    (0...m - 1).each { |i| res += days[i] }
    res
  end
  a1 = to_day.call(arrive_alice)
  a2 = to_day.call(leave_alice)
  b1 = to_day.call(arrive_bob)
  b2 = to_day.call(leave_bob)
  start = [a1, b1].max
  finish = [a2, b2].min
  return 0 if finish < start
  finish - start + 1
end
