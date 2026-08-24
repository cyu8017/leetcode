# LeetCode 2861 - Maximum Number of Alloys
# https://leetcode.com/problems/maximum-number-of-alloys/

# @param {Integer} n
# @param {Integer} k
# @param {Integer} budget
# @param {Integer[][]} composition
# @param {Integer[]} stock
# @param {Integer[]} cost
# @return {Integer}
def max_number_of_alloys(n, k, budget, composition, stock, cost)
  ok = lambda do |machines|
    composition.each do |comp|
      spend = 0
      (0...n).each do |i|
        need = machines * comp[i] - stock[i]
        spend += need * cost[i] if need > 0
      end
      return true if spend <= budget
    end
    false
  end

  lo = 0
  hi = 10**9
  ans = 0
  while lo <= hi
    mid = (lo + hi) / 2
    if ok.call(mid)
      ans = mid
      lo = mid + 1
    else
      hi = mid - 1
    end
  end
  ans
end
