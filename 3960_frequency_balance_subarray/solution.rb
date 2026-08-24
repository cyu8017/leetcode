# LeetCode 3960 - Frequency Balance Subarray
# https://leetcode.com/problems/frequency-balance-subarray/

# @param {Integer[]} nums
# @return {Integer}
def get_length(nums)
  n = nums.length
  ans = 1
  n.times do |l|
    cnt = {}
    freq = {}
    (l...n).each do |r|
      x = nums[r]
      c = cnt.fetch(x, 0)
      if freq.fetch(c, 0) > 0
        fc = freq[c] - 1
        if fc == 0
          freq.delete(c)
        else
          freq[c] = fc
        end
      end
      cnt[x] = c + 1
      freq[cnt[x]] = freq.fetch(cnt[x], 0) + 1
      cx = cnt[x]
      if cnt.length == 1 || (freq.length == 2 && (freq.fetch(cx * 2, 0) > 0 || (cx.even? && freq.fetch(cx / 2, 0) > 0)))
        ans = r - l + 1 if r - l + 1 > ans
      end
    end
  end
  ans
end
