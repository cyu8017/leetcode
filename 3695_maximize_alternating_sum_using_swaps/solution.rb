# LeetCode 3695 - Maximize Alternating Sum Using Swaps
# https://leetcode.com/problems/maximize-alternating-sum-using-swaps/

# @param {Integer[]} nums
# @param {Integer[][]} swaps
# @return {Integer}
def max_alternating_sum(nums, swaps)
  n = nums.length
  parent = (0...n).to_a
  find = nil
  find = lambda do |x|
    parent[x] = find.call(parent[x]) if parent[x] != x
    parent[x]
  end
  swaps.each do |a, b|
    ra = find.call(a)
    rb = find.call(b)
    parent[ra] = rb if ra != rb
  end
  comp_vals = {}
  comp_idx = {}
  (0...n).each do |i|
    r = find.call(i)
    (comp_vals[r] ||= []) << nums[i]
    (comp_idx[r] ||= []) << i
  end
  arr = Array.new(n, 0)
  comp_vals.each do |r, vals|
    idxs = comp_idx[r]
    vals.sort!.reverse!
    even = idxs.select { |i| i.even? }.sort
    odd = idxs.select { |i| i.odd? }.sort
    ei = 0
    vals.each do |v|
      if ei < even.length
        arr[even[ei]] = v
      else
        arr[odd[ei - even.length]] = v
      end
      ei += 1
    end
  end
  ans = 0
  (0...n).each { |i| ans += i.even? ? arr[i] : -arr[i] }
  ans
end
