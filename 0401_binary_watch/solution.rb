# LeetCode 0401 - Binary Watch
# https://leetcode.com/problems/binary-watch/

class Solution
  def read_binary_watch(turned_on)
    result = []
    (0...12).each do |hour|
      (0...60).each do |minute|
        if hour.to_s(2).count("1") + minute.to_s(2).count("1") == turned_on
          result << format("%d:%02d", hour, minute)
        end
      end
    end
    result
  end

  alias_method :readBinaryWatch, :read_binary_watch
end
