# LeetCode 3134 - Find the Median of the Uniqueness Array
# https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/

# @param {Integer[]} nums
# @return {Integer}
def median_of_uniqueness_array(nums)
  n = nums.length
  m = (1 + n) * n / 2

  check = lambda do |mx|
    cnt = {}
    l = 0
    k = 0
    n.times do |r|
      cnt[nums[r]] = cnt.fetch(nums[r], 0) + 1
      while cnt.length > mx
        y = nums[l]
        l += 1
        nv = cnt[y] - 1
        if nv == 0
          cnt.delete(y)
        else
          cnt[y] = nv
        end
      end
      k += r - l + 1
      return true if k >= (m + 1) / 2
    end
    false
  end

  lo = 1
  hi = n
  while lo < hi
    mid = lo + (hi - lo) / 2
    if check.call(mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
