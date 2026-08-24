# LeetCode 3672 - Sum of Weighted Modes in Subarrays
# https://leetcode.com/problems/sum-of-weighted-modes-in-subarrays/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def mode_weight(nums, k)
  cnt = Hash.new(0)
  pq = []
  push = lambda do |freq, val|
    pq << [-freq, val]
  end
  get_mode = lambda do
    loop do
      freq = -pq[0][0]
      val = pq[0][1]
      return freq * val if cnt[val] == freq

      pq.shift
    end
  end
  (0...k).each do |i|
    x = nums[i]
    cnt[x] += 1
    push.call(cnt[x], x)
  end
  pq.sort_by! { |a| [a[0], a[1]] }
  ans = get_mode.call
  (k...nums.length).each do |i|
    x = nums[i]
    y = nums[i - k]
    cnt[x] += 1
    cnt[y] -= 1
    push.call(cnt[x], x)
    push.call(cnt[y], y)
    pq.sort_by! { |a| [a[0], a[1]] }
    ans += get_mode.call
  end
  ans
end
