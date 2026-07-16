# LeetCode 0464 - Can I Win
# https://leetcode.com/problems/can-i-win/

class Solution
  def can_i_win(max_choosable_integer, desired_total)
    return true if desired_total <= 0

    total = max_choosable_integer * (max_choosable_integer + 1) / 2
    return false if total < desired_total

    @memo = {}

    can_win?(0, 0, max_choosable_integer, desired_total)
  end

  alias_method :canIWin, :can_i_win

  private

  def can_win?(state, current_total, max_choosable_integer, desired_total)
    return @memo[state] if @memo.key?(state)

    (1..max_choosable_integer).each do |pick|
      bit = 1 << (pick - 1)
      next if (state & bit) != 0

      return @memo[state] = true if current_total + pick >= desired_total
      return @memo[state] = true unless can_win?(state | bit, current_total + pick, max_choosable_integer, desired_total)
    end

    @memo[state] = false
  end
end
