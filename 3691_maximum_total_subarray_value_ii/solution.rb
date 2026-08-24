# LeetCode 3691 - Maximum Total Subarray Value II
# https://leetcode.com/problems/maximum-total-subarray-value-ii/

class SparseTableRMQ
  def initialize(data)
    @n = data.length
    max_log = 0
    max_log += 1 while (1 << max_log) <= @n
    max_log += 1
    @f_max = Array.new(@n) { Array.new(max_log, 0) }
    @f_min = Array.new(@n) { Array.new(max_log, 0) }
    @lg = Array.new(@n + 1, 0)
    (2..@n).each { |i| @lg[i] = @lg[i >> 1] + 1 }
    (0...@n).each do |i|
      @f_max[i][0] = data[i]
      @f_min[i][0] = data[i]
    end
    (1...max_log).each do |j|
      (0..(@n - (1 << j))).each do |i|
        @f_max[i][j] = [@f_max[i][j - 1], @f_max[i + (1 << (j - 1))][j - 1]].max
        @f_min[i][j] = [@f_min[i][j - 1], @f_min[i + (1 << (j - 1))][j - 1]].min
      end
    end
  end

  def query_max(l, r)
    k = @lg[r - l + 1]
    [@f_max[l][k], @f_max[r - (1 << k) + 1][k]].max
  end

  def query_min(l, r)
    k = @lg[r - l + 1]
    [@f_min[l][k], @f_min[r - (1 << k) + 1][k]].min
  end
end

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_total_value(nums, k)
  n = nums.length
  st = SparseTableRMQ.new(nums)
  pq = []
  (0...n).each do |l|
    val = st.query_max(l, n - 1) - st.query_min(l, n - 1)
    pq << [-val, l, n - 1]
  end
  ans = 0
  k.times do
    pq.sort_by! { |x| x[0] }
    val, l, r = pq.shift
    val = -val
    ans += val
    if r > l
      next_val = st.query_max(l, r - 1) - st.query_min(l, r - 1)
      pq << [-next_val, l, r - 1]
    end
  end
  ans
end
