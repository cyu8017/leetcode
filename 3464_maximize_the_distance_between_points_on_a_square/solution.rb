# LeetCode 3464 - Maximize the Distance Between Points on a Square
# https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/

# @param {Integer} side
# @param {Integer[][]} points
# @param {Integer} k
# @return {Integer}
def max_distance(side, points, k)
  arr = Array.new(points.length, 0)
  points.each_with_index do |(x, y), i|
    arr[i] = if y == 0
               x
             elsif x == side
               side + y
             elsif y == side
               2 * side + (side - x)
             else
               3 * side + (side - y)
             end
  end
  arr.sort!
  perim = 4 * side
  lo = 0
  hi = 2 * side
  while lo < hi
    mid = (lo + hi + 1) / 2
    if can_place_3464(arr, perim, mid, k)
      lo = mid
    else
      hi = mid - 1
    end
  end
  lo
end

def can_place_3464(arr, perim, mid, k)
  n = arr.length
  (0...n).each do |s|
    cnt = 1
    last = arr[s]
    idx = s
    while cnt < k
      target = last + mid
      found = false
      (1...n).each do |step|
        ni = (idx + step) % n
        val = arr[ni]
        add = ni <= idx ? perim : 0
        next unless val + add >= target

        last = val + add
        idx = ni
        cnt += 1
        found = true
        break
      end
      break unless found
    end
    return true if cnt == k && last - arr[s] <= perim - mid
  end
  false
end
