# LeetCode 2106 - Maximum Fruits Harvested After at Most K Steps
# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/

# @param {Integer[][]} fruits
# @param {Integer} start_pos
# @param {Integer} k
# @return {Integer}
def max_total_fruits(fruits, start_pos, k)
  min_steps = lambda do |left, right, start|
    return start - left if right <= start
    return right - start if left >= start

    [(start - left) + (right - left), (right - start) + (right - left)].min
  end

  n = fruits.length
  pref = Array.new(n + 1, 0)
  pos = Array.new(n, 0)
  fruits.each_with_index do |(p, amt), i|
    pos[i] = p
    pref[i + 1] = pref[i] + amt
  end
  ans = 0
  j = 0
  n.times do |i|
    j += 1 while j <= i && min_steps.call(pos[j], pos[i], start_pos) > k
    ans = [ans, pref[i + 1] - pref[j]].max
  end
  ans
end
