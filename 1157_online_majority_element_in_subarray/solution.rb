# LeetCode 1157 - Online Majority Element In Subarray
# https://leetcode.com/problems/online-majority-element-in-subarray/

class MajorityChecker
  def initialize(arr)
    @arr = arr
    @pos = Hash.new { |h, k| h[k] = [] }
    arr.each_with_index { |x, i| @pos[x] << i }
  end

  def query(left, right, threshold)
    candidate = 0
    count = 0
    (left..right).each do |i|
      candidate = @arr[i] if count.zero?
      count += @arr[i] == candidate ? 1 : -1
    end
    locs = @pos[candidate]
    lo = locs.bsearch_index { |x| x >= left } || locs.length
    hi = locs.bsearch_index { |x| x > right } || locs.length
    hi - lo >= threshold ? candidate : -1
  end
end
