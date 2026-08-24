# LeetCode 3753 - Total Waviness of Numbers in Range II
# https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/

# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def total_waviness(a, b)
  waviness_up_to = lambda do |limit|
    return 0 if limit < 0
    digits = []
    if limit == 0
      digits << 0
    else
      value = limit
      while value > 0
        digits << value % 10
        value /= 10
      end
      digits.reverse!
    end
    memo = {}
    dfs = nil
    dfs = lambda do |position, second_last, last, started, tight|
      return [1, 0] if position == digits.length
      key = "#{position},#{second_last},#{last},#{started}"
      return memo[key] if !tight && memo.key?(key)
      upper = tight ? digits[position] : 9
      count = 0
      total = 0
      (0..upper).each do |digit|
        next_tight = tight && digit == upper
        next_second_last = second_last
        next_last = last
        next_started = started || digit != 0
        add = 0
        if !next_started
          next_second_last = next_last = 10
        elsif !started
          next_second_last = 10
          next_last = digit
        else
          if second_last != 10 &&
             ((last > second_last && last > digit) || (last < second_last && last < digit))
            add = 1
          end
          next_second_last = last
          next_last = digit
        end
        child_count, child_sum = dfs.call(position + 1, next_second_last, next_last, next_started, next_tight)
        count += child_count
        total += child_sum + add * child_count
      end
      memo[key] = [count, total] unless tight
      [count, total]
    end
    dfs.call(0, 10, 10, false, true)[1]
  end
  waviness_up_to.call(b) - waviness_up_to.call(a - 1)
end
