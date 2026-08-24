# LeetCode 0683 - K Empty Slots
# https://leetcode.com/problems/k-empty-slots/

# @param {Integer[]} bulbs
# @param {Integer} k
# @return {Integer}
def k_empty_slots(bulbs, k)
  n = bulbs.length
  days = Array.new(n, 0)
  bulbs.each_with_index do |bulb, idx|
    days[bulb - 1] = idx + 1
  end

  ans = Float::INFINITY
  i = 0
  while i < n - k - 1
    left = i
    right = i + k + 1
    j = left + 1
    while j < right && days[j] > days[left] && days[j] > days[right]
      j += 1
    end
    if j == right
      ans = [ans, [days[left], days[right]].max].min
      i += 1
    else
      i = j
    end
  end
  ans == Float::INFINITY ? -1 : ans.to_i
end
