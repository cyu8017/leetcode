# LeetCode 3639 - Minimum Time to Activate String
# https://leetcode.com/problems/minimum-time-to-activate-string/

# @param {String} s
# @param {Integer[]} order
# @param {Integer} k
# @return {Integer}
def min_time(s, order, k)
  n = s.length
  total = n * (n + 1) / 2
  return -1 if k > total

  count_valid = lambda do |t|
    star = Array.new(n, false)
    (0..t).each { |i| star[order[i]] = true }
    invalid = 0
    i = 0
    while i < n
      if star[i]
        i += 1
        next
      end
      j = i
      j += 1 while j < n && !star[j]
      l = j - i
      invalid += l * (l + 1) / 2
      i = j
    end
    total - invalid
  end

  lo = 0
  hi = n - 1
  ans = -1
  while lo <= hi
    mid = (lo + hi) >> 1
    if count_valid.call(mid) >= k
      ans = mid
      hi = mid - 1
    else
      lo = mid + 1
    end
  end
  ans
end
