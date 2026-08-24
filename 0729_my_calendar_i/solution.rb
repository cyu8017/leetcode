# LeetCode 0729 - My Calendar I
# https://leetcode.com/problems/my-calendar-i/

class MyCalendar
  def initialize
    @bookings = []
  end

  def book(start_time, end_time)
    @bookings.each do |start, finish|
      return false if start < end_time && start_time < finish
    end
    @bookings << [start_time, end_time]
    true
  end
end
