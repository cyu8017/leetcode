# LeetCode 2763 - Sum of Imbalance Numbers of All Subarrays
# https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def sum_imbalance_numbers(nums)
  n = nums.length
  ans = 0
  (0...n).each do |i|
    seen = {}
    sorted_vals = []
    imbalance = 0
    (i...n).each do |j|
      x = nums[j]
      unless seen[x]
        seen[x] = true
        lo = 0
        hi = sorted_vals.length
        while lo < hi
          mid = (lo + hi) >> 1
          if sorted_vals[mid] < x
            lo = mid + 1
          else
            hi = mid
          end
        end
        nxt = lo < sorted_vals.length ? sorted_vals[lo] : nil
        prev = lo > 0 ? sorted_vals[lo - 1] : nil
        imbalance += 1 if !prev.nil? && x - prev != 1
        imbalance += 1 if !nxt.nil? && nxt - x != 1
        imbalance -= 1 if !prev.nil? && !nxt.nil? && nxt - prev > 1
        sorted_vals.insert(lo, x)
      end
      ans += imbalance
    end
  end
  ans
end
