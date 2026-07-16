# LeetCode 0335 - Self Crossing
# https://leetcode.com/problems/self-crossing/

class Solution
  def is_self_crossing(distance)
    (3...distance.length).each do |index|
      if distance[index] >= distance[index - 2] && distance[index - 1] <= distance[index - 3]
        return true
      end
      if index >= 4 && distance[index - 1] == distance[index - 3]
        if distance[index - 2] >= distance[index - 4] + distance[index]
          return true
        end
      end
      if index >= 5
        if distance[index - 4] >= distance[index - 2] - distance[index]
          if distance[index] >= distance[index - 2] - distance[index - 4]
            if distance[index - 1] <= distance[index - 3]
              if distance[index - 5] + distance[index - 1] >= distance[index - 3]
                return true
              end
            end
          end
        end
      end
    end
    false
  end

  alias_method :isSelfCrossing, :is_self_crossing
end
