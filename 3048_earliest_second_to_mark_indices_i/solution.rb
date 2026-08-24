# LeetCode 3048 - Earliest Second to Mark Indices I
# https://leetcode.com/problems/earliest-second-to-mark-indices-i/

# @param {Integer[]} nums
# @param {Integer[]} change_indices
# @return {Integer}
def earliest_second_to_mark_indices(nums, change_indices)
  n = nums.length
  m = change_indices.length
  ok = lambda do |t|
    last = Array.new(n + 1, 0)
    t.times { |s| last[change_indices[s]] = s }
    decrement = 0
    marked = 0
    t.times do |s|
      i = change_indices[s]
      if last[i] == s
        return false if decrement < nums[i - 1]

        decrement -= nums[i - 1]
        marked += 1
      else
        decrement += 1
      end
    end
    marked == n
  end
  l = 0
  r = m + 1
  while l < r
    mid = (l + r) >> 1
    if ok.call(mid)
      r = mid
    else
      l = mid + 1
    end
  end
  l > m ? -1 : l
end
