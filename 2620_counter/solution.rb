# LeetCode 2620 - Counter
# https://leetcode.com/problems/counter/

# @param {Integer} n
# @return {Proc}
def create_counter(n)
  lambda do
    v = n
    n += 1
    v
  end
end
