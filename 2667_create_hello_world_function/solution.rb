# LeetCode 2667 - Create Hello World Function
# https://leetcode.com/problems/create-hello-world-function/

# @return {Proc}
def create_hello_world
  lambda { |*_args| "Hello World" }
end
