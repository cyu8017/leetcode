# LeetCode 2821 - Delay the Resolution of Each Promise
# https://leetcode.com/problems/delay-the-resolution-of-each-promise/

# @param {Proc[]} functions
# @param {Integer} ms
# @return {Proc[]}
def delay_all(functions, ms)
  functions.map do |fn|
    lambda do
      fn.respond_to?(:call) ? fn.call : fn
    end
  end
end
