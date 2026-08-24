# LeetCode 2195 - Append K Integers With Minimal Sum
# https://leetcode.com/problems/append-k-integers-with-minimal-sum/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def minimal_k_sum(nums, k)
  nums = nums.sort
  ans = 0
  prev = 0
  nums.each do |x|
    next if x <= prev

    start = prev + 1
    finish = x - 1
    if start <= finish
      cnt = finish - start + 1
      if cnt > k
        finish = start + k - 1
        cnt = k
      end
      ans += (start + finish) * cnt / 2
      k -= cnt
      return ans if k == 0
    end
    prev = x
  end
  s = prev + 1
  e = s + k - 1
  ans + (s + e) * k / 2
end
