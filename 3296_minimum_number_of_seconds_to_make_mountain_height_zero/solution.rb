# LeetCode 3296 - Minimum Number of Seconds to Make Mountain Height Zero
# https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/

# @param {Integer} t
# @param {Integer} mountain_height
# @param {Integer[]} worker_times
# @return {Boolean}
def mountain_seconds_ok(t, mountain_height, worker_times)
  total = 0
  worker_times.each do |w|
    l = 0
    h = mountain_height
    while l < h
      mid = (l + h + 1) / 2
      if w * mid * (mid + 1) / 2 <= t
        l = mid
      else
        h = mid - 1
      end
    end
    total += l
    return true if total >= mountain_height
  end
  total >= mountain_height
end

# @param {Integer} mountain_height
# @param {Integer[]} worker_times
# @return {Integer}
def min_number_of_seconds(mountain_height, worker_times)
  lo = 0
  hi = 10**18
  while lo < hi
    mid = (lo + hi) / 2
    if mountain_seconds_ok(mid, mountain_height, worker_times)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
