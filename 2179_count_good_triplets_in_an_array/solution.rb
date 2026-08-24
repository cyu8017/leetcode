# LeetCode 2179 - Count Good Triplets in an Array
# https://leetcode.com/problems/count-good-triplets-in-an-array/

class Fenwick
  def initialize(sz)
    @bit = Array.new(sz, 0)
  end

  def add(i, v)
    while i < @bit.length
      @bit[i] += v
      i += i & -i
    end
  end

  def sum(i)
    s = 0
    while i > 0
      s += @bit[i]
      i -= i & -i
    end
    s
  end
end

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def good_triplets(nums1, nums2)
  n = nums1.length
  pos2 = Array.new(n, 0)
  n.times { |i| pos2[nums2[i]] = i }
  mapped = Array.new(n, 0)
  n.times { |i| mapped[i] = pos2[nums1[i]] }
  left = Array.new(n, 0)
  right = Array.new(n, 0)
  fw = Fenwick.new(n + 2)
  n.times do |i|
    left[i] = fw.sum(mapped[i])
    fw.add(mapped[i] + 1, 1)
  end
  fw = Fenwick.new(n + 2)
  (n - 1).downto(0) do |i|
    right[i] = fw.sum(n) - fw.sum(mapped[i] + 1)
    fw.add(mapped[i] + 1, 1)
  end
  ans = 0
  n.times { |i| ans += left[i] * right[i] }
  ans
end
