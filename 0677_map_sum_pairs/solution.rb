# LeetCode 0677 - Map Sum Pairs
# https://leetcode.com/problems/map-sum-pairs/

class MapSum
  def initialize
    @values = {}
    @prefix_sums = Hash.new(0)
  end

  def insert(key, val)
    delta = val - (@values[key] || 0)
    @values[key] = val
    (1..key.length).each do |i|
      prefix = key[0, i]
      @prefix_sums[prefix] += delta
    end
    nil
  end

  def sum(prefix)
    @prefix_sums[prefix]
  end
end
