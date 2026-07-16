# LeetCode 0466 - Count The Repetitions
# https://leetcode.com/problems/count-the-repetitions/

class Solution
  def get_max_repetitions(s1, n1, s2, n2)
    return 0 if s2.empty?

    index = 0
    s2_count = 0
    record = {}

    n1.times do |repeat|
      s1.each_char do |char|
        next unless char == s2[index]

        index += 1
        if index == s2.length
          index = 0
          s2_count += 1
        end
      end

      if record.key?(index)
        previous_repeat, previous_count = record[index]
        cycle = repeat - previous_repeat
        count_cycle = s2_count - previous_count
        remaining = n1 - repeat - 1
        s2_count += (remaining / cycle) * count_cycle
        break if repeat + (remaining / cycle) * cycle >= n1 - 1
      end
      record[index] = [repeat, s2_count]
    end

    s2_count / n2
  end

  alias_method :getMaxRepetitions, :get_max_repetitions
end
