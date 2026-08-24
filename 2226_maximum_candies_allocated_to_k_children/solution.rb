# LeetCode 2226 - Maximum Candies Allocated to K Children
# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

# @param {Integer[]} candies
# @param {Integer} k
# @return {Integer}
def maximum_candies(candies, k)
  lo = 0
  hi = candies.empty? ? 0 : candies.max
  can = lambda do |mid|
    return true if mid == 0

    cnt = 0
    candies.each do |c|
      cnt += c / mid
      return true if cnt >= k
    end
    false
  end
  while lo < hi
    mid = (lo + hi + 1) / 2
    if can.call(mid)
      lo = mid
    else
      hi = mid - 1
    end
  end
  lo
end
