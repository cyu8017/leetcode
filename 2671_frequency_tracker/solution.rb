# LeetCode 2671 - Frequency Tracker
# https://leetcode.com/problems/frequency-tracker/

class FrequencyTracker
  def initialize
    @freq = Hash.new(0)
    @count = Hash.new(0)
  end

  def add(number)
    old = @freq[number]
    @count[old] -= 1 if old > 0
    @freq[number] = old + 1
    @count[old + 1] += 1
    nil
  end

  def delete_one(number)
    old = @freq[number]
    return if old == 0

    @count[old] -= 1
    @freq[number] = old - 1
    @count[old - 1] += 1 if old - 1 > 0
    nil
  end

  def has_frequency(frequency)
    @count[frequency] > 0
  end
end
