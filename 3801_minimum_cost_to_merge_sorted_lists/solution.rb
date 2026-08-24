# LeetCode 3801 - Minimum Cost to Merge Sorted Lists
# https://leetcode.com/problems/minimum-cost-to-merge-sorted-lists/

# @param {Integer[][]} lists
# @return {Integer}
def min_merge_cost(lists)
  m = lists.length
  total_masks = 1 << m
  merged = Array.new(total_masks) { [] }
  length = Array.new(total_masks, 0)
  median = Array.new(total_masks, 0)
  trailing_zeros = lambda do |bit|
    n = 0
    while (bit & 1) == 0
      bit >>= 1
      n += 1
    end
    n
  end
  (1...total_masks).each do |mask|
    bit = mask & -mask
    index = trailing_zeros.call(bit)
    previous = merged[mask ^ bit]
    current = lists[index]
    out = []
    i = 0
    j = 0
    while i < previous.length || j < current.length
      if j == current.length || (i < previous.length && previous[i] <= current[j])
        out << previous[i]
        i += 1
      else
        out << current[j]
        j += 1
      end
    end
    merged[mask] = out
    length[mask] = out.length
    median[mask] = out[(out.length - 1) / 2]
  end
  inf = 10**18
  dp = Array.new(total_masks, 0)
  (1...total_masks).each do |mask|
    next if (mask & (mask - 1)) == 0
    dp[mask] = inf
    first_bit = mask & -mask
    left = (mask - 1) & mask
    while left > 0
      if (left & first_bit) != 0
        right = mask ^ left
        if right != 0
          diff = median[left] - median[right]
          diff = -diff if diff < 0
          candidate = dp[left] + dp[right] + length[mask] + diff
          dp[mask] = candidate if candidate < dp[mask]
        end
      end
      left = (left - 1) & mask
    end
  end
  dp[total_masks - 1]
end
