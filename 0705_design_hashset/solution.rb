# LeetCode 0705 - Design HashSet
# https://leetcode.com/problems/design-hashset/

class MyHashSet
  def initialize
    @data = {}
  end

  def add(key)
    @data[key] = true
    nil
  end

  def remove(key)
    @data.delete(key)
    nil
  end

  def contains(key)
    @data.key?(key)
  end
end
