
MOD = 10**9 + 7

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def min_absolute_sum_diff(nums1, nums2)
  sorted_nums1 = nums1.sort
  total = nums1.zip(nums2).sum { |a, b| (a - b).abs }
  best_gain = 0

  nums2.each_with_index do |target, i|
    current = (nums1[i] - target).abs
    idx = sorted_nums1.bsearch_index { |x| x >= target } || sorted_nums1.length
    [idx - 1, idx].each do |j|
      next unless j >= 0 && j < sorted_nums1.length
      gain = current - (sorted_nums1[j] - target).abs
      best_gain = gain if gain > best_gain
    end
  end

  (total - best_gain) % MOD
end
