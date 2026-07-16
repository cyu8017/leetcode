# LeetCode 0370 - Range Addition
# https://leetcode.com/problems/range-addition/

class Solution
  def get_modified_array(length, updates)
    diff = Array.new(length + 1, 0)

    updates.each do |start, finish, inc|
      diff[start] += inc
      diff[finish + 1] -= inc if finish + 1 < diff.length
    end

    result = Array.new(length, 0)
    running = 0
    length.times do |index|
      running += diff[index]
      result[index] = running
    end

    result
  end

  alias_method :getModifiedArray, :get_modified_array
end
