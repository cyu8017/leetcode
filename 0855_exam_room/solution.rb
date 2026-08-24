# LeetCode 0855 - Exam Room
# https://leetcode.com/problems/exam-room/

class ExamRoom
  def initialize(n)
    @n = n
    @seats = []
  end

  def seat
    if @seats.empty?
      @seats << 0
      return 0
    end

    best_seat = 0
    best_dist = @seats[0]
    (1...@seats.length).each do |i|
      dist = (@seats[i] - @seats[i - 1]) / 2
      if dist > best_dist
        best_dist = dist
        best_seat = @seats[i - 1] + dist
      end
    end
    best_seat = @n - 1 if @n - 1 - @seats[-1] > best_dist
    idx = @seats.bsearch_index { |x| x >= best_seat } || @seats.length
    @seats.insert(idx, best_seat)
    best_seat
  end

  def leave(p)
    @seats.delete(p)
    nil
  end
end
