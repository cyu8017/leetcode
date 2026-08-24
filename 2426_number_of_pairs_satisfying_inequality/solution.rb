# LeetCode 2426 - Number of Pairs Satisfying Inequality
# https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} diff
# @return {Integer}
def number_of_pairs(nums1, nums2, diff)
  n = nums1.length
  arr = Array.new(n) { |i| nums1[i] - nums2[i] }
  tmp = Array.new(n, 0)

  merge_count = lambda do |l, r|
    return 0 if r - l <= 1

    m = (l + r) >> 1
    ans = merge_count.call(l, m) + merge_count.call(m, r)
    j = m
    (l...m).each do |i|
      j += 1 while j < r && arr[j] < arr[i] - diff
      ans += r - j
    end
    p = l
    q = m
    i2 = l
    while p < m && q < r
      if arr[p] <= arr[q]
        tmp[i2] = arr[p]
        p += 1
      else
        tmp[i2] = arr[q]
        q += 1
      end
      i2 += 1
    end
    while p < m
      tmp[i2] = arr[p]
      p += 1
      i2 += 1
    end
    while q < r
      tmp[i2] = arr[q]
      q += 1
      i2 += 1
    end
    (l...r).each { |t| arr[t] = tmp[t] }
    ans
  end

  merge_count.call(0, n)
end
