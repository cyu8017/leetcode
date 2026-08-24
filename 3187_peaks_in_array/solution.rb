# LeetCode 3187 - Peaks in Array
# https://leetcode.com/problems/peaks-in-array/

class BIT
  def initialize(n)
    @n = n
    @c = Array.new(n + 1, 0)
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
# @param {Integer[][]} queries
# @return {Integer[]}
def count_of_peaks(nums, queries)
  n = nums.length
  tree = BIT.new(n - 1)
  update_peak = lambda do |i, val|
    return if i <= 0 || i >= n - 1
    tree.update(i, val) if nums[i - 1] < nums[i] && nums[i] > nums[i + 1]
  end
  (1...n - 1).each { |i| update_peak.call(i, 1) }
  ans = []
  queries.each do |q|
    if q[0] == 1
      l = q[1] + 1
      r = q[2] - 1
      t = 0
      t = tree.query(r) - tree.query(l - 1) if l <= r
      ans << t
    else
      idx = q[1]
      val = q[2]
      (idx - 1..idx + 1).each { |i| update_peak.call(i, -1) }
      nums[idx] = val
      (idx - 1..idx + 1).each { |i| update_peak.call(i, 1) }
    end
  end
  ans
end
