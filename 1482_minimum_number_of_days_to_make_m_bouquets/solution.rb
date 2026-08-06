# LeetCode 1482 - Minimum Number Of Days To Make M Bouquets
# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

def min_days(bloom_day, m, k)
  return -1 if m * k > bloom_day.length
  possible = lambda do |day|
    bouquets = run = 0
    bloom_day.each do |x|
      run = x <= day ? run + 1 : 0
      if run == k
        bouquets += 1
        run = 0
      end
    end
    bouquets >= m
  end
  lo = bloom_day.min
  hi = bloom_day.max
  while lo < hi
    mid = (lo + hi) / 2
    if possible.call(mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
