# LeetCode 0432 - All O`one` Data Structure
# https://leetcode.com/problems/all-oone-data-structure/

require "set"

class CountNode
  attr_accessor :count, :keys, :prev, :next

  def initialize(count = 0)
    @count = count
    @keys = Set.new
    @prev = nil
    @next = nil
  end
end

class AllOne
  def initialize
    @head = CountNode.new
    @tail = CountNode.new
    @head.next = @tail
    @tail.prev = @head
    @key_nodes = {}
  end

  def inc(key)
    if @key_nodes.key?(key)
      bucket = @key_nodes[key]
      bucket.keys.delete(key)
      next_bucket = ensure_count_node(bucket.count + 1, bucket)
      next_bucket.keys.add(key)
      @key_nodes[key] = next_bucket
      remove(bucket) if bucket.keys.empty?
      return
    end

    bucket = ensure_count_node(1, @head)
    bucket.keys.add(key)
    @key_nodes[key] = bucket
  end

  def dec(key)
    bucket = @key_nodes[key]
    bucket.keys.delete(key)
    if bucket.count == 1
      @key_nodes.delete(key)
    else
      prev_bucket = ensure_count_node(bucket.count - 1, @head)
      prev_bucket.keys.add(key)
      @key_nodes[key] = prev_bucket
    end
    remove(bucket) if bucket.keys.empty?
  end

  def get_max_key
    bucket = @tail.prev
    return "" if bucket == @head

    bucket.keys.first
  end

  def get_min_key
    bucket = @head.next
    return "" if bucket == @tail

    bucket.keys.first
  end

  alias_method :getMaxKey, :get_max_key
  alias_method :getMinKey, :get_min_key

  private

  def insert_after(anchor, node)
    node.prev = anchor
    node.next = anchor.next
    anchor.next.prev = node
    anchor.next = node
  end

  def remove(node)
    node.prev.next = node.next
    node.next.prev = node.prev
  end

  def ensure_count_node(count, after)
    current = after.next
    while current != @tail && current.count < count
      current = current.next
    end
    return current if current != @tail && current.count == count

    bucket = CountNode.new(count)
    insert_after(current.prev, bucket)
    bucket
  end
end
