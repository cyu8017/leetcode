# LeetCode 1326 - Minimum Number Of Taps To Open To Water A Garden
# https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/

def min_taps(n, ranges)
  farthest = Array.new(n + 1, 0)
  ranges.each_with_index do |radius, center|
    left = [0, center - radius].max
    right = [n, center + radius].min
    farthest[left] = [farthest[left], right].max
  end
  taps = 0
  ending = 0
  reach = 0
  n.times do |position|
    reach = [reach, farthest[position]].max
    if position == ending
      return -1 if reach <= position
      taps += 1
      ending = reach
    end
  end
  taps
end
