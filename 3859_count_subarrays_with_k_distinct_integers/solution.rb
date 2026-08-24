# LeetCode 3859 - Count Subarrays With K Distinct Integers
# https://leetcode.com/problems/count-subarrays-with-k-distinct-integers/

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} m
# @return {Integer}
def count_subarrays(nums, k, m)
  f = lambda do |lim|
    cnt = Hash.new(0)
    ans = 0
    l = 0
    t = 0
    nums.each do |x|
      c = cnt[x] + 1
      cnt[x] = c
      t += 1 if c == m
      while cnt.length >= lim && t >= k
        y = nums[l]
        l += 1
        cy = cnt[y] - 1
        t -= 1 if cy == m - 1
        if cy == 0
          cnt.delete(y)
        else
          cnt[y] = cy
        end
      end
      ans += l
    end
    ans
  end
  f.call(k) - f.call(k + 1)
end
