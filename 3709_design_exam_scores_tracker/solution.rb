# LeetCode 3709 - Design Exam Scores Tracker
# https://leetcode.com/problems/design-exam-scores-tracker/

class ExamTracker
  def initialize
    @times = [0]
    @pre = [0]
  end

  def record(time, score)
    @times << time
    @pre << @pre[-1] + score
  end

  def total_score(start_time, end_time)
    l = bisect_left(@times, start_time) - 1
    r = bisect_left(@times, end_time + 1) - 1
    @pre[r] - @pre[l]
  end

  private

  def bisect_left(a, target)
    lo = 0
    hi = a.length
    while lo < hi
      mid = (lo + hi) >> 1
      if a[mid] < target
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
end
