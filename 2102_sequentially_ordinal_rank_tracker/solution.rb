# LeetCode 2102 - Sequentially Ordinal Rank Tracker
# https://leetcode.com/problems/sequentially-ordinal-rank-tracker/

class SORTracker
  def initialize
    @items = []
    @k = 0
  end

  def add(name, score)
    @items << [score, name]
    @items.sort_by! { |s, n| [-s, n] }
    nil
  end

  def get
    @k += 1
    @items[@k - 1][1]
  end
end
