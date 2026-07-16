# LeetCode 0341 - Flatten Nested List Iterator
# https://leetcode.com/problems/flatten-nested-list-iterator/

class NestedInteger
  def initialize(value = nil)
    if value.is_a?(Integer)
      @integer = value
      @list = []
    else
      @integer = nil
      @list = []
    end
  end

  def is_integer
    !@integer.nil?
  end

  def get_integer
    @integer || 0
  end

  def get_list
    @list
  end

  alias_method :isInteger, :is_integer
  alias_method :getInteger, :get_integer
  alias_method :getList, :get_list
end

class NestedIterator
  def initialize(nested_list)
    @stack = []
    nested_list.reverse_each do |item|
      @stack.push([item, 0])
    end
  end

  def next
    prepare_next
    current, = @stack.pop
    current.get_integer
  end

  def has_next
    prepare_next
    !@stack.empty?
  end

  alias_method :hasNext, :has_next

  private

  def prepare_next
    while !@stack.empty?
      current, index = @stack.last
      return if current.is_integer

      nested = current.get_list
      if index >= nested.length
        @stack.pop
        next
      end
      @stack[-1] = [current, index + 1]
      @stack.push([nested[index], 0])
    end
  end
end
