# LeetCode 3410 - Maximize Subarray Sum After Removing All Occurrences of One Element
# https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/

# @param {Integer[]} nums
# @return {Integer}
def max_subarray_sum(nums)
  ans = kadane_3410(nums)
  uniq = {}
  nums.each { |x| uniq[x] = true if x < 0 }
  uniq.each_key do |v|
    b = nums.select { |x| x != v }
    next if b.empty?

    cand = kadane_3410(b)
    ans = cand if cand > ans
  end
  ans
end

def kadane_3410(a)
  best = -9_007_199_254_740_991
  cur = 0
  a.each do |x|
    cur += x
    best = cur if cur > best
    cur = 0 if cur < 0
  end
  all_neg = true
  mx = a[0]
  a.each do |x|
    mx = x if x > mx
    all_neg = false if x >= 0
  end
  return mx if all_neg

  best
end
