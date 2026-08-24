# LeetCode 0895 - Maximum Frequency Stack
# https://leetcode.com/problems/maximum-frequency-stack/

class FreqStack
  def initialize
    @freq = Hash.new(0)
    @group = Hash.new { |h, k| h[k] = [] }
    @maxfreq = 0
  end

  def push(val)
    f = @freq[val] + 1
    @freq[val] = f
    @maxfreq = f if f > @maxfreq
    @group[f] << val
    nil
  end

  def pop
    val = @group[@maxfreq].pop
    @freq[val] -= 1
    @maxfreq -= 1 if @group[@maxfreq].empty?
    val
  end
end
