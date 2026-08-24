# LeetCode 2797 - Partial Function with Placeholders
# https://leetcode.com/problems/partial-function-with-placeholders/

# @param {Proc} fn
# @param {Object[]} args
# @return {Proc}
def partial(fn, args)
  lambda do |*rest_args|
    full = []
    ri = 0
    args.each do |a|
      if a == "_"
        if ri < rest_args.length
          full << rest_args[ri]
          ri += 1
        end
      else
        full << a
      end
    end
    while ri < rest_args.length
      full << rest_args[ri]
      ri += 1
    end
    fn.call(*full)
  end
end
