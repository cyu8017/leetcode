# LeetCode 2776 - Convert Callback Based Function to Promise Based Function
# https://leetcode.com/problems/convert-callback-based-function-to-promise-based-function/

# @param {Proc} fn
# @return {Proc}
def promisify(fn)
  lambda do |*args|
    err = nil
    result = nil
    callback = lambda do |e, r = nil|
      err = e
      result = r
    end
    fn.call(callback, *args)
    raise err if err
    result
  end
end
