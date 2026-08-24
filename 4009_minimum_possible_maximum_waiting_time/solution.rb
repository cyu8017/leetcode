# LeetCode 4009 - Minimum Possible Maximum Waiting Time
# https://leetcode.com/problems/minimum-possible-maximum-waiting-time/

# @param {Integer[]} demand
# @param {Integer[]} fuel
# @return {Integer}
def min_max_waiting_time(demand, fuel)
  pack_key = lambda { |i, f0, f1, d0, d1| ((((i * 51 + f0) * 51 + f1) * 21 + d0) * 21 + d1) }
  dem = demand
  n = dem.length
  f0, f1 = fuel[0], fuel[1]
  return -1 if f0 < demand[0] && f1 < demand[0]
  memo = {}
  max_serve = nil
  max_serve = lambda do |i, ff0, ff1, d0, d1|
    return i if i == n
    key = pack_key.call(i, ff0, ff1, d0, d1)
    return memo[key] if memo.key?(key)
    need = dem[i]
    can0 = ff0 >= need
    can1 = ff1 >= need
    best = i
    if !can0 && !can1
      memo[key] = best
      return best
    end
    if can0
      nd1 = d1 > d0 ? d1 - d0 : 0
      v = max_serve.call(i + 1, ff0 - need, ff1, need, nd1)
      best = v if v > best
    end
    if can1
      nd0 = d0 > d1 ? d0 - d1 : 0
      v = max_serve.call(i + 1, ff0, ff1 - need, nd0, need)
      best = v if v > best
    end
    memo[key] = best
    best
  end
  best_serve = max_serve.call(0, f0, f1, 0, 0)
  return -1 if best_serve == 0
  can_with_w = nil
  w = 0
  can_with_w = lambda do |i, ff0, ff1, d0, d1|
    return true if i >= best_serve || i == n
    key = pack_key.call(i, ff0, ff1, d0, d1)
    return memo[key] == 2 if memo.key?(key)
    need = dem[i]
    can0 = ff0 >= need
    can1 = ff1 >= need
    ok = false
    if !can0 && !can1
      memo[key] = 1
      return false
    end
    if can0 && d0 <= w
      nd1 = d1 > d0 ? d1 - d0 : 0
      ok = true if can_with_w.call(i + 1, ff0 - need, ff1, need, nd1)
    end
    if !ok && can1 && d1 <= w
      nd0 = d0 > d1 ? d0 - d1 : 0
      ok = true if can_with_w.call(i + 1, ff0, ff1 - need, nd0, need)
    end
    memo[key] = ok ? 2 : 1
    ok
  end
  lo = 0
  hi = demand.sum
  ans = hi
  while lo <= hi
    mid = (lo + hi) / 2
    w = mid
    memo = {}
    if can_with_w.call(0, f0, f1, 0, 0)
      ans = mid
      hi = mid - 1
    else
      lo = mid + 1
    end
  end
  ans
end
