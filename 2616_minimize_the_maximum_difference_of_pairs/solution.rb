# LeetCode 2616 - Minimize the Maximum Difference of Pairs
# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/

# @param {Integer[]} nums
# @param {Integer} p
# @return {Integer}
def minimize_max(nums, p)
  nums = nums.sort
  lo = 0
  hi = nums[-1] - nums[0]

  ok = lambda do |d|
    cnt = 0
    i = 0
    while i + 1 < nums.length
      if nums[i + 1] - nums[i] <= d
        cnt += 1
        i += 2
      else
        i += 1
      end
    end
    cnt >= p
  end

  while lo < hi
    mid = (lo + hi) >> 1
    if ok.call(mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
