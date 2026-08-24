# LeetCode 2516 - Take K of Each Character From Left and Right
# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def take_characters(s, k)
  n = s.length
  cnt = [0, 0, 0]
  s.each_byte { |b| cnt[b - 97] += 1 }
  return -1 if cnt[0] < k || cnt[1] < k || cnt[2] < k

  need = [cnt[0] - k, cnt[1] - k, cnt[2] - k]
  window = [0, 0, 0]
  left = 0
  max_mid = 0
  (0...n).each do |right|
    window[s[right].ord - 97] += 1
    while window[0] > need[0] || window[1] > need[1] || window[2] > need[2]
      window[s[left].ord - 97] -= 1
      left += 1
    end
    max_mid = right - left + 1 if right - left + 1 > max_mid
  end
  n - max_mid
end
