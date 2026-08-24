# LeetCode 2691 - Immutability Helper
# https://leetcode.com/problems/immutability-helper/

class ImmutableHelper
  def initialize(obj)
    @obj = obj
  end

  def produce(mutator)
    clones = {}
    is_obj = lambda { |v| v.is_a?(Hash) || v.is_a?(Array) }
    get_clone = lambda do |original|
      oid = original.object_id
      return clones[oid] if clones.key?(oid)

      copy = original.is_a?(Array) ? original.dup : original.dup
      clones[oid] = copy
      copy
    end
    root_result = [@obj]
    proxy = nil
    proxy = lambda do |node, on_replace|
      obj = Object.new
      obj.define_singleton_method(:[]) do |prop|
        val = node[prop]
        if is_obj.call(val)
          child_replace = lambda do |child_clone|
            clone = get_clone.call(node)
            clone[prop] = child_clone
            on_replace.call(clone)
          end
          return proxy.call(val, child_replace)
        end
        val
      end
      obj.define_singleton_method(:[]=) do |prop, value|
        clone = get_clone.call(node)
        clone[prop] = value
        on_replace.call(clone)
      end
      obj.define_singleton_method(:delete) do |prop|
        clone = get_clone.call(node)
        clone.delete(prop)
        on_replace.call(clone)
      end
      obj
    end
    on_root = lambda { |clone| root_result[0] = clone }
    mutator.call(proxy.call(@obj, on_root))
    root_result[0]
  end
end

# @param {Object} obj
# @param {Object} mutators
# @return {ImmutableHelper}
def immutable_helper(obj, _mutators = nil)
  ImmutableHelper.new(obj)
end

def solve(*args)
  immutable_helper(*args)
end
