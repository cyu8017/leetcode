# LeetCode 1756 - Design Most Recently Used Queue
# https://leetcode.com/problems/design-most-recently-used-queue/

class MRUQueue
  # @param {Integer} n
  def initialize(n)
    @q = (1..n).to_a
  end

  # @param {Integer} k
  # @return {Integer}
  def fetch(k)
    val = @q.delete_at(k - 1)
    @q << val
    val
  end
end
