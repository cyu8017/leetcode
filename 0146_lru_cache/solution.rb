class Node
  attr_accessor :key, :value, :prev, :next

  def initialize(key = 0, value = 0)
    @key = key
    @value = value
  end
end

class LRUCache
  def initialize(capacity)
    @capacity = capacity
    @cache = {}
    @head = Node.new
    @tail = Node.new
    @head.next = @tail
    @tail.prev = @head
  end

  def get(key)
    return -1 unless @cache.key?(key)

    node = @cache[key]
    remove(node)
    add_to_front(node)
    node.value
  end

  def put(key, value)
    if @cache.key?(key)
      node = @cache[key]
      node.value = value
      remove(node)
      add_to_front(node)
      return
    end

    if @cache.length == @capacity
      least_recent = @tail.prev
      remove(least_recent)
      @cache.delete(least_recent.key)
    end

    node = Node.new(key, value)
    @cache[key] = node
    add_to_front(node)
  end

  private

  def remove(node)
    node.prev.next = node.next
    node.next.prev = node.prev
  end

  def add_to_front(node)
    node.prev = @head
    node.next = @head.next
    @head.next.prev = node
    @head.next = node
  end
end