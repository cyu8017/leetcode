# LeetCode 2632 - Curry
# https://leetcode.com/problems/curry/

# @param {Proc} fn
# @return {Proc}
def curry(fn)
  arity = fn.arity
  arity = arity.abs - 1 if arity.negative?
  curried = nil
  curried = lambda do |*args|
    return fn.call(*args) if args.length >= arity

    lambda { |*next_args| curried.call(*args, *next_args) }
  end
  curried
end

def solve(*args)
  curry(*args)
end
