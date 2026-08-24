# LeetCode 3824 - Minimum K to Reduce Array Within Limit
# https://leetcode.com/problems/minimum-k-to-reduce-array-within-limit/

# @param {Integer[]} nums
# @return {Integer}
def minimum_k(nums)
  lo = 1
  hi = 100000
  while lo < hi
    mid = (lo + hi) / 2
    if check_k_limit(nums, mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end

def check_k_limit(nums, k)
  t = 0
  nums.each { |x| t += (x + k - 1) / k }
  t <= k * k
end
