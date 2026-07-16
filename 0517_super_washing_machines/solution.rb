# LeetCode 0517 - Super Washing Machines
# https://leetcode.com/problems/super-washing-machines/

class Solution
  def find_min_moves(machines)
    total = machines.sum
    count = machines.length
    return -1 if total % count != 0

    target = total / count
    prefix = 0
    result = 0

    machines.each do |clothes|
      diff = clothes - target
      prefix += diff
      result = [result, prefix.abs, diff].max
    end

    result
  end

  alias_method :findMinMoves, :find_min_moves
end
