# LeetCode 0385 - Mini Parser
# https://leetcode.com/problems/mini-parser/

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
  def deserialize(s)
    return NestedInteger.new(s.to_i) unless s.start_with?("[")

    stack = []
    current = nil
    index = 0
    negative = false
    number = 0
    has_number = false

    while index < s.length
      char = s[index]
      case char
      when "["
        item = NestedInteger.new
        stack << current unless current.nil?
        current = item
      when "-"
        negative = true
      when "0".."9"
        number = number * 10 + char.to_i
        has_number = true
      when ",", "]"
        if has_number
          value = negative ? -number : number
          current.get_list << NestedInteger.new(value)
          number = 0
          negative = false
          has_number = false
        end
        if char == "]"
          return current if stack.empty?

          parent = stack.pop
          parent.get_list << current
          current = parent
        end
      end
      index += 1
    end

    current || NestedInteger.new
  end
end
