# LeetCode 0493 - Reverse Pairs
# https://leetcode.com/problems/reverse-pairs/

class Solution
  def reverse_pairs(nums)
    merge_sort = lambda do |start, finish|
      return 0 if start >= finish

      mid = (start + finish) / 2
      count = merge_sort.call(start, mid) + merge_sort.call(mid + 1, finish)
      j = mid + 1
      (start..mid).each do |i|
        while j <= finish && nums[i] > 2 * nums[j]
          j += 1
        end
        count += j - (mid + 1)
      end
      nums[start..finish] = nums[start..finish].sort
      count
    end

    merge_sort.call(0, nums.length - 1)
  end

  alias_method :reversePairs, :reverse_pairs
end
