# LeetCode 0253 - Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-ii/

# @param {Integer[][]} intervals
# @return {Integer}
def min_meeting_rooms(intervals)
  starts = intervals.map { |interval| interval[0] }.sort
  ends = intervals.map { |interval| interval[1] }.sort
  rooms = 0
  max_rooms = 0
  start_index = 0
  end_index = 0

  while start_index < starts.length
    if starts[start_index] < ends[end_index]
      rooms += 1
      max_rooms = [max_rooms, rooms].max
      start_index += 1
    else
      rooms -= 1
      end_index += 1
    end
  end

  max_rooms
end
