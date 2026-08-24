# LeetCode 0706 - Design HashMap
# https://leetcode.com/problems/design-hashmap/

class MyHashMap
  def initialize
    @data = {}
  end

  def put(key, value)
    @data[key] = value
    nil
  end

  def get(key)
    @data.fetch(key, -1)
  end

  def remove(key)
    @data.delete(key)
    nil
  end
end
