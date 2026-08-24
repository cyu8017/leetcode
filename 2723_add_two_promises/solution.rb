# LeetCode 2723 - Add Two Promises
# https://leetcode.com/problems/add-two-promises/

# @param {Object} promise1
# @param {Object} promise2
# @return {Object}
def add_two_promises(promise1, promise2)
  resolve = lambda do |p|
    p.respond_to?(:call) ? p.call : p
  end
  resolve.call(promise1) + resolve.call(promise2)
end

def solve(*args)
  add_two_promises(*args)
end
