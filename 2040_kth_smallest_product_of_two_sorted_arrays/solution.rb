# LeetCode 2040 - Kth Smallest Product of Two Sorted Arrays
# https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} k
# @return {Integer}
def kth_smallest_product(nums1, nums2, k)
  count_le = lambda do |x|
    cnt = 0
    nums1.each do |a|
      if a > 0
        lo = 0
        hi = nums2.length
        while lo < hi
          mid = (lo + hi) >> 1
          if a * nums2[mid] <= x
            lo = mid + 1
          else
            hi = mid
          end
        end
        cnt += lo
      elsif a < 0
        lo = 0
        hi = nums2.length
        while lo < hi
          mid = (lo + hi) >> 1
          if a * nums2[mid] <= x
            hi = mid
          else
            lo = mid + 1
          end
        end
        cnt += nums2.length - lo
      elsif x >= 0
        cnt += nums2.length
      end
    end
    cnt
  end

  lo = -10**10
  hi = 10**10
  while lo < hi
    mid = lo + (hi - lo) / 2
    if count_le.call(mid) >= k
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
