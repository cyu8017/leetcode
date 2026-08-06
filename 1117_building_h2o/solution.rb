# LeetCode 1117 - Building H2O
# https://leetcode.com/problems/building-h2o/

class H2O
  def initialize
    @h = 0
    @o = 0
    @mutex = Mutex.new
    @cv = ConditionVariable.new
  end

  def hydrogen(release_hydrogen)
    @mutex.synchronize do
      @cv.wait(@mutex) until @h < 2
      release_hydrogen.call
      @h += 1
      reset_if_ready
      @cv.broadcast
    end
  end

  def oxygen(release_oxygen)
    @mutex.synchronize do
      @cv.wait(@mutex) until @o < 1
      release_oxygen.call
      @o += 1
      reset_if_ready
      @cv.broadcast
    end
  end

  private

  def reset_if_ready
    return unless @h == 2 && @o == 1
    @h = 0
    @o = 0
  end
end
