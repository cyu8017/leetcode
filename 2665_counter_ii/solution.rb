# LeetCode 2665 - Counter II
# https://leetcode.com/problems/counter-ii/

# @param {Integer} init
# @return {Hash}
def create_counter(init)
  cur = init
  {
    "increment" => lambda {
      cur += 1
      cur
    },
    "decrement" => lambda {
      cur -= 1
      cur
    },
    "reset" => lambda {
      cur = init
      cur
    }
  }
end
