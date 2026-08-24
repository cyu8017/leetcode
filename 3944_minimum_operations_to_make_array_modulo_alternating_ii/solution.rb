# LeetCode 3944 - Minimum Operations to Make Array Modulo Alternating II
# https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-ii/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_operations(nums, k)
  costs = lambda do |freq, k|
    dbl = Array.new(2 * k, 0)
    (2 * k).times { |i| dbl[i] = freq[i % k] }
    count_prefix = Array.new(2 * k + 1, 0)
    weighted_prefix = Array.new(2 * k + 1, 0)
    (2 * k).times do |i|
      count_prefix[i + 1] = count_prefix[i] + dbl[i]
      weighted_prefix[i + 1] = weighted_prefix[i] + i * dbl[i]
    end
    res = Array.new(k, 0)
    cw = k / 2
    cc = (k - 1) / 2
    k.times do |t|
      cnt = count_prefix[t + cw + 1] - count_prefix[t]
      s = weighted_prefix[t + cw + 1] - weighted_prefix[t]
      res[t] += s - t * cnt
      if cc > 0
        cnt2 = count_prefix[t + k] - count_prefix[t + k - cc]
        sum2 = weighted_prefix[t + k] - weighted_prefix[t + k - cc]
        res[t] += (t + k) * cnt2 - sum2
      end
    end
    res
  end
  even_freq = Array.new(k, 0)
  odd_freq = Array.new(k, 0)
  nums.each_with_index do |v, i|
    if i.even?
      even_freq[v % k] += 1
    else
      odd_freq[v % k] += 1
    end
  end
  even_cost = costs.call(even_freq, k)
  odd_cost = costs.call(odd_freq, k)
  best1 = 1 << 62
  best2 = 1 << 62
  best_index = -1
  k.times do |i|
    x = odd_cost[i]
    if x < best1
      best2 = best1
      best1 = x
      best_index = i
    elsif x < best2
      best2 = x
    end
  end
  ans = 1 << 62
  k.times do |x|
    other = x == best_index ? best2 : best1
    v = even_cost[x] + other
    ans = v if v < ans
  end
  ans
end
