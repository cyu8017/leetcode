# LeetCode 2141 - Maximum Running Time of N Computers
# https://leetcode.com/problems/maximum-running-time-of-n-computers/

# @param {Integer} n
# @param {Integer[]} batteries
# @return {Integer}
def max_run_time(n, batteries)
  sum = batteries.sum
  lo = 1
  hi = sum / n
  while lo < hi
    mid = (lo + hi + 1) / 2
    need = batteries.sum { |b| [b, mid].min }
    if need >= mid * n
      lo = mid
    else
      hi = mid - 1
    end
  end
  lo
end
