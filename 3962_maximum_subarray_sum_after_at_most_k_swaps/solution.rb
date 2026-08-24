# LeetCode 3962 - Maximum Subarray Sum After at Most K Swaps
# https://leetcode.com/problems/maximum-subarray-sum-after-at-most-k-swaps/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_subarray_sum(nums, k)
  unique = nums.sort
  u = 0
  unique.each_with_index do |v, i|
    if u == 0 || v != unique[u - 1]
      unique[u] = v
      u += 1
    end
  end
  unique = unique[0...u]
  n = nums.length
  lower_bound = lambda do |a, x|
    lo = 0
    hi = a.length
    while lo < hi
      mid = (lo + hi) / 2
      if a[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
  add = lambda do |count, s, index, delta|
    value = unique[index - 1]
    while index < count.length
      count[index] += delta
      s[index] += delta * value
      index += index & -index
    end
  end
  query_count = lambda do |bit, index|
    result = 0
    while index > 0
      result += bit[index]
      index -= index & -index
    end
    result
  end
  query_sum = lambda do |bit, index|
    result = 0
    while index > 0
      result += bit[index]
      index -= index & -index
    end
    result
  end
  kth = lambda do |bit, order|
    index = 0
    step = 1
    step <<= 1 while (step << 1) < bit.length
    while step > 0
      nxt = index + step
      if nxt < bit.length && bit[nxt] < order
        index = nxt
        order -= bit[nxt]
      end
      step >>= 1
    end
    index + 1
  end
  sum_smallest = lambda do |count, s, amount|
    return 0 if amount <= 0
    index = kth.call(count, amount)
    count_before = query_count.call(count, index - 1)
    sum_before = query_sum.call(s, index - 1)
    sum_before + (amount - count_before) * unique[index - 1]
  end
  rank = Array.new(n, 0)
  global_count = Array.new(unique.length + 1, 0)
  global_sum = Array.new(unique.length + 1, 0)
  n.times do |i|
    rank[i] = lower_bound.call(unique, nums[i]) + 1
    add.call(global_count, global_sum, rank[i], 1)
  end
  answer = -(1 << 60)
  n.times do |left|
    inside_count = Array.new(unique.length + 1, 0)
    inside_sum = Array.new(unique.length + 1, 0)
    outside_count = global_count.dup
    outside_sum = global_sum.dup
    subarray_sum = 0
    (left...n).each do |right|
      add.call(outside_count, outside_sum, rank[right], -1)
      add.call(inside_count, inside_sum, rank[right], 1)
      subarray_sum += nums[right]
      inside_size = right - left + 1
      outside_size = n - inside_size
      limit = [k, [inside_size, outside_size].min].min
      low = 0
      high = limit
      while low < high
        mid = (low + high + 1) / 2
        inside_value = unique[kth.call(inside_count, mid) - 1]
        outside_order = outside_size - mid + 1
        outside_value = unique[kth.call(outside_count, outside_order) - 1]
        if outside_value > inside_value
          low = mid
        else
          high = mid - 1
        end
      end
      swaps = low
      gain = 0
      if swaps > 0
        small_inside = sum_smallest.call(inside_count, inside_sum, swaps)
        total_outside = query_sum.call(outside_sum, unique.length)
        large_outside = total_outside - sum_smallest.call(outside_count, outside_sum, outside_size - swaps)
        gain = large_outside - small_inside
      end
      v = subarray_sum + gain
      answer = v if v > answer
    end
  end
  answer
end
