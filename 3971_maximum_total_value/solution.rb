# LeetCode 3971 - Maximum Total Value
# https://leetcode.com/problems/maximum-total-value/

# @param {Integer[]} value
# @param {Integer[]} decay
# @param {Integer} m
# @return {Integer}
def maximum_total_value(value, decay, m)
  count_at_least = lambda do |threshold|
    count = 0
    value.each_with_index do |v, i|
      count += (v - threshold) / decay[i] + 1 if v >= threshold
    end
    count
  end
  mod = 1_000_000_007
  if count_at_least.call(1) <= m
    s = 0
    value.each_with_index do |v, i|
      terms = (v - 1) / decay[i] + 1
      s = (s + terms * v - decay[i] * terms * (terms - 1) / 2) % mod
    end
    return s
  end
  high = value.max
  low = 1
  while low < high
    mid = (low + high + 1) / 2
    if count_at_least.call(mid) >= m
      low = mid
    else
      high = mid - 1
    end
  end
  threshold = low
  count = 0
  s = 0
  value.each_with_index do |v, i|
    next if v < threshold
    terms = (v - threshold) / decay[i] + 1
    count += terms
    s = (s + (terms * v - decay[i] * terms * (terms - 1) / 2) % mod) % mod
  end
  s = (s - ((count - m) % mod) * (threshold % mod)) % mod
  s += mod if s < 0
  s
end
