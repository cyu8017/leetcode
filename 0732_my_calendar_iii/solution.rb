# LeetCode 0732 - My Calendar III
# https://leetcode.com/problems/my-calendar-iii/

class MyCalendarThree
  def initialize
    @delta = Hash.new(0)
  end

  def book(start_time, end_time)
    @delta[start_time] += 1
    @delta[end_time] -= 1
    current = 0
    best = 0
    @delta.keys.sort.each do |time|
      current += @delta[time]
      best = [best, current].max
    end
    best
  end
end
