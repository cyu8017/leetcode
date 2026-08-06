# LeetCode 1964 - Find the Longest Valid Obstacle Course at Each Position
# https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

# @param {Integer[]} obstacles
# @return {Integer[]}
def longest_obstacle_course_at_each_position(obstacles)
  tails = []
  ans = []
  obstacles.each do |x|
    lo = 0
    hi = tails.length
    while lo < hi
      mid = (lo + hi) / 2
      if tails[mid] <= x
        lo = mid + 1
      else
        hi = mid
      end
    end
    i = lo
    if i == tails.length
      tails << x
    else
      tails[i] = x
    end
    ans << i + 1
  end
  ans
end
