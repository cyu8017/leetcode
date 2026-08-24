# LeetCode 2692 - Make Object Immutable
# https://leetcode.com/problems/make-object-immutable/

class ImmutableList < Array
  MUTATORS = %w[pop append push concat insert delete clear sort! reverse!].freeze

  def []=(index, _value)
    raise "Error Modifying Index: #{index}"
  end

  def delete_at(index)
    raise "Error Modifying Index: #{index}"
  end

  def method_missing(name, *args, &blk)
    raise "Error Calling Method: #{name}" if MUTATORS.include?(name.to_s)

    super
  end
end

class ImmutableDict < Hash
  def []=(key, _value)
    raise "Error Modifying: #{key}"
  end

  def delete(key)
    raise "Error Modifying: #{key}"
  end
end

# @param {Object} obj
# @return {Object}
def make_immutable(obj)
  wrap = nil
  wrap = lambda do |val|
    return val if val.nil? || !(val.is_a?(Hash) || val.is_a?(Array))
    return ImmutableList.new(val.map { |x| wrap.call(x) }) if val.is_a?(Array)

    ImmutableDict[val.map { |k, v| [k, wrap.call(v)] }]
  end
  wrap.call(obj)
end

def solve(*args)
  make_immutable(*args)
end
