# LeetCode 2122 - Recover the Original Array
# https://leetcode.com/problems/recover-the-original-array/

# @param {Integer[]} nums
# @return {Integer[]}
def recover_array(nums)
  nums = nums.sort
  n = nums.length
  (1...n).each do |i|
    diff = nums[i] - nums[0]
    next if diff == 0 || diff.odd?

    k = diff / 2
    used = Array.new(n, false)
    used[0] = used[i] = true
    ans = [(nums[0] + nums[i]) / 2]
    l = 0
    r = i
    ok = true
    while ans.length < n / 2
      l += 1 while l < n && used[l]
      if l == n
        ok = false
        break
      end
      need = nums[l] + 2 * k
      r += 1 while r < n && (used[r] || nums[r] < need)
      if r == n || nums[r] != need
        ok = false
        break
      end
      used[l] = used[r] = true
      ans << nums[l] + k
    end
    return ans if ok
  end
  []
end
