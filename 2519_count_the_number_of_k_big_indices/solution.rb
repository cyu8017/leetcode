# LeetCode 2519 - Count the Number of K-Big Indices
# https://leetcode.com/problems/count-the-number-of-k-big-indices/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def k_big_indices(nums, k)
  n = nums.length
  uniq = nums.sort
  m = 0
  uniq.each_index do |i|
    if i == 0 || uniq[i] != uniq[i - 1]
      uniq[m] = uniq[i]
      m += 1
    end
  end
  rank = {}
  (0...m).each { |i| rank[uniq[i]] = i + 1 }
  left = Array.new(n, 0)
  right = Array.new(n, 0)

  add = lambda do |bit, i, v|
    while i < bit.length
      bit[i] += v
      i += i & -i
    end
  end

  sum_ft = lambda do |bit, i|
    s = 0
    while i > 0
      s += bit[i]
      i -= i & -i
    end
    s
  end

  ft = Array.new(m + 2, 0)
  (0...n).each do |i|
    r = rank[nums[i]]
    left[i] = sum_ft.call(ft, r - 1)
    add.call(ft, r, 1)
  end
  ft = Array.new(m + 2, 0)
  (n - 1).downto(0) do |i|
    r = rank[nums[i]]
    right[i] = sum_ft.call(ft, r - 1)
    add.call(ft, r, 1)
  end
  ans = 0
  (0...n).each { |i| ans += 1 if left[i] >= k && right[i] >= k }
  ans
end
