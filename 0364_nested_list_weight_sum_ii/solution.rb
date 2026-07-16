# LeetCode 0364 - Nested List Weight Sum II
# https://leetcode.com/problems/nested-list-weight-sum-ii/

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

class Solution
  def depth_sum(nested_list)
    nested_list = json_to_nested_list(nested_list) unless nested_list.empty? || nested_list.first.is_a?(NestedInteger)
    weighted = []

    dfs = lambda do |items, depth|
      items.each do |item|
        if item.is_integer
          weighted << [item.get_integer, depth]
        else
          dfs.call(item.get_list, depth + 1)
        end
      end
    end

    dfs.call(nested_list, 1)
    return 0 if weighted.empty?

    max_depth = weighted.map(&:last).max
    weighted.sum { |value, depth| value * (max_depth - depth + 1) }
  end

  alias_method :depthSum, :depth_sum

  private

  def json_to_nested_integer(value)
    return NestedInteger.new(value) if value.is_a?(Integer)

    item = NestedInteger.new
    value.each do |entry|
      item.get_list << json_to_nested_integer(entry)
    end
    item
  end

  def json_to_nested_list(values)
    values.map { |value| json_to_nested_integer(value) }
  end
end
