# LeetCode 2627 - Debounce
# https://leetcode.com/problems/debounce/

# @param {Proc} fn
# @param {Integer} t
# @return {Proc}
def debounce(fn, t)
  timer = { id: nil }
  lambda do |*args|
    timer[:id] = { args: args, t: t }
    fn.call(*args)
  end
end
