# LeetCode 0452 - Minimum Number of Arrows to Burst Balloons
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution
  def find_min_arrow_shots(points)
    return 0 if points.empty?

    sorted = points.sort_by { |point| point[1] }
    arrows = 1
    end_time = sorted[0][1]

    sorted.drop(1).each do |start, finish|
      if start > end_time
        arrows += 1
        end_time = finish
      end
    end

    arrows
  end

  alias_method :findMinArrowShots, :find_min_arrow_shots
end
