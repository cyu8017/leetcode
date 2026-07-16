# LeetCode 0434 - Number of Segments in a String
# https://leetcode.com/problems/number-of-segments-in-a-string/

class Solution
  def count_segments(s)
    count = 0
    in_segment = false
    s.each_char do |char|
      if char != " "
        unless in_segment
          count += 1
          in_segment = true
        end
      else
        in_segment = false
      end
    end
    count
  end

  alias_method :countSegments, :count_segments
end
