# LeetCode 1670 - Design Front Middle Back Queue
# https://leetcode.com/problems/design-front-middle-back-queue/

class FrontMiddleBackQueue
  def initialize
    @l = []
    @r = []
  end

  def _bal
    while @l.length > @r.length + 1
      @r.unshift(@l.pop)
    end
    while @r.length > @l.length
      @l << @r.shift
    end
  end

  # @param {Integer} val
  # @return {Void}
  def push_front(val)
    @l.unshift(val)
    _bal
  end

  # @param {Integer} val
  # @return {Void}
  def push_middle(val)
    @r.unshift(@l.pop) if @l.length > @r.length
    @l << val
  end

  # @param {Integer} val
  # @return {Void}
  def push_back(val)
    @r << val
    _bal
  end

  # @return {Integer}
  def pop_front
    return -1 if @l.empty?

    v = @l.shift
    _bal
    v
  end

  # @return {Integer}
  def pop_middle
    return -1 if @l.empty?

    v = @l.pop
    _bal
    v
  end

  # @return {Integer}
  def pop_back
    return -1 if @l.empty?

    v = @r.empty? ? @l.pop : @r.pop
    _bal
    v
  end
end
