# LeetCode 3169 - Count Days Without Meetings
# https://leetcode.com/problems/count-days-without-meetings/

# @param {Integer} days
# @param {Integer[][]} meetings
# @return {Integer}
def count_days(days, meetings)
  meetings = meetings.sort_by { |e| e[0] }
  last = 0
  ans = 0
  meetings.each do |st, ed|
    ans += st - last - 1 if last < st
    last = [last, ed].max
  end
  ans + days - last
end
