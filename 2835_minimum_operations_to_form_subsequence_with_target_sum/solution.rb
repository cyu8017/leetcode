# LeetCode 2835 - Minimum Operations to Form Subsequence With Target Sum
# https://leetcode.com/problems/minimum-operations-to-form-subsequence-with-target-sum/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def min_operations(nums, target)
  cnt = Array.new(32, 0)
  total = 0
  nums.each do |v|
    total += v
    b = 0
    b += 1 while (1 << b) < v
    cnt[b] += 1
  end
  return -1 if total < target

  ans = 0
  (0...31).each do |i|
    if (target & (1 << i)) != 0
      if cnt[i] > 0
        cnt[i] -= 1
      else
        j = i + 1
        j += 1 while j < 32 && cnt[j] == 0
        return -1 if j == 32

        while j > i
          cnt[j] -= 1
          cnt[j - 1] += 2
          ans += 1
          j -= 1
        end
        cnt[i] -= 1
      end
    end
    cnt[i + 1] += cnt[i] / 2
  end
  ans
end
