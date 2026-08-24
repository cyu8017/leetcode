# LeetCode 3369 - Design an Array Statistics Tracker
# https://leetcode.com/problems/design-an-array-statistics-tracker/

class StatisticsTracker
  def initialize
    @arr = []
    @sum = 0
    @freq = {}
    @mode_freq = 0
    @modes = {}
  end

  def add_number(num)
    @arr << num
    @sum += num
    f = (@freq[num] || 0) + 1
    @freq[num] = f
    if f > @mode_freq
      @mode_freq = f
      @modes.clear
      @modes[num] = true
    elsif f == @mode_freq
      @modes[num] = true
    end
    nil
  end

  def remove_first
    return if @arr.empty?

    num = @arr.shift
    @sum -= num
    f = @freq[num] - 1
    if f == 0
      @freq.delete(num)
    else
      @freq[num] = f
    end
    @mode_freq = 0
    @modes.clear
    @freq.each do |v, ff|
      if ff > @mode_freq
        @mode_freq = ff
        @modes.clear
        @modes[v] = true
      elsif ff == @mode_freq
        @modes[v] = true
      end
    end
    nil
  end

  def get_mean
    return 0 if @arr.empty?

    @sum / @arr.length
  end

  def get_median
    n = @arr.length
    tmp = @arr.sort
    return tmp[n / 2] if n.odd?

    tmp[n / 2 - 1]
  end

  def get_mode
    best = 9_007_199_254_740_991
    @modes.each_key { |v| best = v if v < best }
    best == 9_007_199_254_740_991 ? 0 : best
  end
end
