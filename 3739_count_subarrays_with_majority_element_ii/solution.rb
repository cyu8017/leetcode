# LeetCode 3739 - Count Subarrays With Majority Element II
# https://leetcode.com/problems/count-subarrays-with-majority-element-ii/

class MajorityBit
  def initialize(n_)
    @n = n_
    @c = Array.new(n_ + 1, 0)
  end

  def update(x, delta)
    while x <= @n
      @c[x] += delta
      x += x & -x
    end
  end

  def query(x)
    s = 0
    while x > 0
      s += @c[x]
      x -= x & -x
    end
    s
  end
end

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def count_majority_subarrays(nums, target)
  n = nums.length
  tree = MajorityBit.new(2 * n + 1)
  s = n + 1
  tree.update(s, 1)
  ans = 0
  nums.each do |x|
    s += x == target ? 1 : -1
    ans += tree.query(s - 1)
    tree.update(s, 1)
  end
  ans
end
