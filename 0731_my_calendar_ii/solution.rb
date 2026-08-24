# LeetCode 0731 - My Calendar II
# https://leetcode.com/problems/my-calendar-ii/

class MyCalendarTwo
  def initialize
    @booked = []
    @overlaps = []
  end

  def book(start_time, end_time)
    @overlaps.each do |start, finish|
      return false if start < end_time && start_time < finish
    end
    @booked.each do |start, finish|
      if start < end_time && start_time < finish
        @overlaps << [[start, start_time].max, [finish, end_time].min]
      end
    end
    @booked << [start_time, end_time]
    true
  end
end
