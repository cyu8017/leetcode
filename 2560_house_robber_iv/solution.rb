# LeetCode 2560 - House Robber IV
# https://leetcode.com/problems/house-robber-iv/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_capability(nums, k)
  lo = nums.min
  hi = nums.max

  ok = lambda do |cap|
    cnt = 0
    i = 0
    while i < nums.length
      if nums[i] <= cap
        cnt += 1
        i += 2
      else
        i += 1
      end
    end
    cnt >= k
  end

  while lo < hi
    mid = (lo + hi) / 2
    if ok.call(mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
