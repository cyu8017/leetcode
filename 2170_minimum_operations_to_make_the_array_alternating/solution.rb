# LeetCode 2170 - Minimum Operations to Make the Array Alternating
# https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/

# @param {Integer[]} nums
# @return {Integer}
def minimum_operations(nums)
  n = nums.length
  return 0 if n == 1

  top2 = lambda do |idxs|
    freq = Hash.new(0)
    idxs.each { |i| freq[nums[i]] += 1 }
    a = ac = b = bc = 0
    freq.each do |v, c|
      if c > ac
        b = a
        bc = ac
        a = v
        ac = c
      elsif c > bc
        b = v
        bc = c
      end
    end
    [a, ac, b, bc]
  end

  even = []
  odd = []
  n.times { |i| (i.even? ? even : odd) << i }
  e = top2.call(even)
  o = top2.call(odd)
  return n - e[1] - o[1] if e[0] != o[0]

  [n - e[1] - o[3], n - e[3] - o[1]].min
end
