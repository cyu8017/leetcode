# LeetCode 2557 - Maximum Number of Integers to Choose From a Range II
# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-ii/

# @param {Integer[]} banned
# @param {Integer} n
# @param {Integer} max_sum
# @return {Integer}
def max_count(banned, n, max_sum)
  banned = banned.sort
  uniq = []
  banned.each do |x|
    uniq << x if x >= 1 && x <= n && (uniq.empty? || uniq[-1] != x)
  end
  ans = 0
  remain = max_sum
  prev = 0

  check = lambda do |l, r|
    return if l > r || remain <= 0

    lo = l
    hi = r
    best = l - 1
    while lo <= hi
      mid = (lo + hi) / 2
      cnt = mid - l + 1
      s = (l + mid) * cnt / 2
      if s <= remain
        best = mid
        lo = mid + 1
      else
        hi = mid - 1
      end
    end
    if best >= l
      cnt = best - l + 1
      ans += cnt
      remain -= (l + best) * cnt / 2
    end
  end

  uniq.each do |b|
    check.call(prev + 1, b - 1)
    prev = b
  end
  check.call(prev + 1, n)
  ans
end

alias solve max_count
