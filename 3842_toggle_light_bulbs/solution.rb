# LeetCode 3842 - Toggle Light Bulbs
# https://leetcode.com/problems/toggle-light-bulbs/

# @param {Integer[]} bulbs
# @return {Integer[]}
def toggle_light_bulbs(bulbs)
  st = Array.new(101, 0)
  bulbs.each { |x| st[x] ^= 1 }
  ans = []
  (0...101).each { |i| ans << i if st[i] == 1 }
  ans
end
