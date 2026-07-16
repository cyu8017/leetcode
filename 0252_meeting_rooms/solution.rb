# LeetCode 0252 - Meeting Rooms
# https://leetcode.com/problems/meeting-rooms/

# @param {Integer[][]} intervals
# @return {Boolean}
def can_attend_meetings(intervals)
  intervals.sort_by { |interval| interval[0] }
  intervals.each_cons(2) do |previous, current|
    return false if current[0] < previous[1]
  end
  true
end
