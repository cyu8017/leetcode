# LeetCode 3907 - Count Smaller Elements With Opposite Parity
# https://leetcode.com/problems/count-smaller-elements-with-opposite-parity/

class BIT3907
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
# @return {Integer[]}
def count_smaller_opposite_parity(nums)
  n = nums.length
  sorted_nums = nums.sort
  m = 0
  sorted_nums.length.times do |i|
    if i == 0 || sorted_nums[i] != sorted_nums[i - 1]
      sorted_nums[m] = sorted_nums[i]
      m += 1
    end
  end
  sorted_nums = sorted_nums[0, m]
  bits = [BIT3907.new(m), BIT3907.new(m)]
  ans = Array.new(n, 0)
  (n - 1).downto(0) do |i|
    lo = 0
    hi = sorted_nums.length
    while lo < hi
      mid = (lo + hi) >> 1
      if sorted_nums[mid] < nums[i]
        lo = mid + 1
      else
        hi = mid
      end
    end
    x = lo + 1
    ans[i] = bits[(nums[i] & 1) ^ 1].query(x - 1)
    bits[nums[i] & 1].update(x, 1)
  end
  ans
end

alias new_bit count_smaller_opposite_parity
