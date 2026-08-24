# LeetCode 3086 - Minimum Moves to Pick K Ones
# https://leetcode.com/problems/minimum-moves-to-pick-k-ones/

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} max_changes
# @return {Integer}
def minimum_moves(nums, k, max_changes)
  n = nums.length
  cnt = Array.new(n + 1, 0)
  s = Array.new(n + 1, 0)
  (1..n).each do |i|
    cnt[i] = cnt[i - 1] + nums[i - 1]
    s[i] = s[i - 1] + i * nums[i - 1]
  end
  ans = 10**18
  (1..n).each do |i|
    t = 0
    need = k - nums[i - 1]
    [i - 1, i + 1].each do |j|
      if need > 0 && j >= 1 && j <= n && nums[j - 1] == 1
        need -= 1
        t += 1
      end
    end
    c = [need, max_changes].min
    need -= c
    t += c * 2
    if need <= 0
      ans = [ans, t].min
      next
    end
    l = 2
    r = [i - 1, n - i].max
    while l <= r
      mid = (l + r) >> 1
      l1 = [1, i - mid].max
      r1 = [0, i - 2].max
      l2 = [n + 1, i + 2].min
      r2 = [n, i + mid].min
      c1 = cnt[r1] - cnt[l1 - 1]
      c2 = cnt[r2] - cnt[l2 - 1]
      if c1 + c2 >= need
        t1 = c1 * i - (s[r1] - s[l1 - 1])
        t2 = s[r2] - s[l2 - 1] - c2 * i
        ans = [ans, t + t1 + t2].min
        r = mid - 1
      else
        l = mid + 1
      end
    end
  end
  ans
end
