# LeetCode 1552 - Magnetic Force Between Two Balls
# https://leetcode.com/problems/magnetic-force-between-two-balls/

# @param {Integer[]} position
# @param {Integer} m
# @return {Integer}
def max_distance(position, m)
  position = position.sort
  lo = 1
  hi = (position[-1] - position[0]) / (m - 1)
  while lo <= hi
    mid = (lo + hi) / 2
    count = 1
    last = position[0]
    position[1..].each do |x|
      if x - last >= mid
        count += 1
        last = x
      end
    end
    if count >= m
      lo = mid + 1
    else
      hi = mid - 1
    end
  end
  hi
end
