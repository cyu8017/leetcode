# LeetCode 2926 - Maximum Balanced Subsequence Sum
# https://leetcode.com/problems/maximum-balanced-subsequence-sum/

# @param {Integer[]} nums
# @return {Integer}
def max_balanced_subsequence_sum(nums)
  neg_inf = -(2**53) / 4
  n = nums.length
  keys = nums.each_with_index.map { |v, i| v - i }
  uniq = keys.uniq.sort
  bit = Array.new(uniq.length + 2, neg_inf)

  idx_of = lambda do |v|
    lo = 0
    hi = uniq.length
    while lo < hi
      mid = (lo + hi) / 2
      if uniq[mid] < v
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo + 1
  end

  update = lambda do |i, val|
    while i < bit.length
      bit[i] = val if val > bit[i]
      i += i & -i
    end
  end

  query = lambda do |i|
    best = neg_inf
    while i > 0
      best = bit[i] if bit[i] > best
      i -= i & -i
    end
    best
  end

  ans = neg_inf
  (0...n).each do |i|
    id_ = idx_of.call(keys[i])
    best = query.call(id_)
    cur = nums[i]
    if best > neg_inf / 2
      cand = best + nums[i]
      cur = cand if cand > cur
    end
    update.call(id_, cur)
    ans = cur if cur > ans
  end
  ans
end
