# LeetCode 0362 - Design Hit Counter
# https://leetcode.com/problems/design-hit-counter/

class HitCounter
  def initialize
    @hits = []
  end

  def hit(timestamp)
    @hits << timestamp
  end

  def get_hits(timestamp)
    while !@hits.empty? && @hits[0] <= timestamp - 300
      @hits.shift
    end
    @hits.length
  end

  alias_method :getHits, :get_hits
end
