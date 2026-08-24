# LeetCode 2690 - Infinite Method Object
# https://leetcode.com/problems/infinite-method-object/

class InfiniteObject
  def method_missing(*_args, **_kwargs)
    "Hello World"
  end

  def respond_to_missing?(_name, _include_private = false)
    true
  end
end

# @return {InfiniteObject}
def create_infinite_object
  InfiniteObject.new
end

def solve(*args)
  create_infinite_object(*args)
end
