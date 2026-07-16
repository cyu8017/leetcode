# LeetCode 0488 - Zuma Game
# https://leetcode.com/problems/zuma-game/

class Solution
  def find_min_step(board, hand)
    @memo = {}

    shrink = lambda do |s|
      i = 0
      while i < s.length
        j = i
        j += 1 while j < s.length && s[j] == s[i]
        if j - i >= 3
          return shrink.call(s[0, i] + s[j..])
        end
        i = j
      end
      s
    end

    dfs = lambda do |b, h|
      key = [b, h]
      return @memo[key] if @memo.key?(key)

      b = shrink.call(b)
      return 0 if b.empty?

      best = Float::INFINITY
      (0..b.length).each do |i|
        h.each_char.with_index do |color, j|
          next if i < b.length && b[i] == color
          next if i.positive? && b[i - 1] == color

          new_b = shrink.call(b[0, i] + color + b[i..])
          next if new_b == b

          new_h = h[0, j] + h[(j + 1)..]
          steps = dfs.call(new_b, new_h)
          best = [best, steps + 1].min unless steps == Float::INFINITY
        end
      end
      @memo[key] = best
    end

    result = dfs.call(board, hand)
    result == Float::INFINITY ? -1 : result
  end

  alias_method :findMinStep, :find_min_step
end
