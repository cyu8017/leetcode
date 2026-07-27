# LeetCode 1649 - Create Sorted Array through Instructions
# https://leetcode.com/problems/create-sorted-array-through-instructions/

# @param {Integer[]} instructions
# @return {Integer}
def create_sorted_array(instructions)
  mod = 1_000_000_007
  size = (instructions.max || 0) + 2
  bit = Array.new(size + 1, 0)
  query = lambda do |i|
    s = 0
    while i.positive?
      s += bit[i]
      i -= i & -i
    end
    s
  end
  ans = 0
  instructions.each_with_index do |x, i|
    ans = (ans + [query.call(x - 1), i - query.call(x)].min) % mod
    j = x
    while j <= size
      bit[j] += 1
      j += j & -j
    end
  end
  ans
end
