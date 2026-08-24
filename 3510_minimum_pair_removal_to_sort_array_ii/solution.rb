# LeetCode 3510 - Minimum Pair Removal to Sort Array II
# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/

# @param {Integer[]} nums
# @return {Integer}
def minimum_pair_removal(nums)
  n = nums.length
  inv = 0
  ans = 0
  sl = []
  idx = {}
  (0...n).each { |i| idx[i] = true }
  sl_map = {}

  key = lambda { |sm, i| sm * 1000000007 + i }

  add_sl = lambda do |sm, i|
    sl_map[key.call(sm, i)] = [sm, i]
    lo = 0
    hi = sl.length
    while lo < hi
      mid = (lo + hi) >> 1
      if sl[mid][0] < sm || (sl[mid][0] == sm && sl[mid][1] < i)
        lo = mid + 1
      else
        hi = mid
      end
    end
    sl.insert(lo, [sm, i])
  end

  rem_sl = lambda do |sm, i|
    k = key.call(sm, i)
    return unless sl_map.key?(k)
    sl_map.delete(k)
    (0...sl.length).each do |t|
      if sl[t][0] == sm && sl[t][1] == i
        sl.delete_at(t)
        break
      end
    end
  end

  ceiling = lambda do |st, x|
    best = nil
    st.each_key do |v|
      best = v if v >= x && (best.nil? || v < best)
    end
    best
  end

  floor = lambda do |st, x|
    best = nil
    st.each_key do |v|
      best = v if v <= x && (best.nil? || v > best)
    end
    best
  end

  (0...(n - 1)).each do |i|
    inv += 1 if nums[i] > nums[i + 1]
    add_sl.call(nums[i] + nums[i + 1], i)
  end
  while inv > 0
    ans += 1
    p = sl.shift
    sl_map.delete(key.call(p[0], p[1]))
    s = p[0]
    i = p[1]
    j = ceiling.call(idx, i + 1)
    inv -= 1 if nums[i] > nums[j]
    h = floor.call(idx, i - 1)
    unless h.nil?
      inv -= 1 if nums[h] > nums[i]
      rem_sl.call(nums[h] + nums[i], h)
      inv += 1 if nums[h] > s
      add_sl.call(nums[h] + s, h)
    end
    kk = ceiling.call(idx, j + 1)
    unless kk.nil?
      inv -= 1 if nums[j] > nums[kk]
      rem_sl.call(nums[j] + nums[kk], j)
      inv += 1 if s > nums[kk]
      add_sl.call(s + nums[kk], i)
    end
    nums[i] = s
    idx.delete(j)
  end
  ans
end
