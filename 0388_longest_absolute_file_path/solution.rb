# LeetCode 0388 - Longest Absolute File Path
# https://leetcode.com/problems/longest-absolute-file-path/

class Solution
  def length_longest_path(input)
    stack = []
    max_length = 0

    input.split("\n").each do |line|
      depth = line.count("\t")
      name = line[depth..]
      stack.pop while stack.length > depth

      if name.include?(".")
        total = name.length + (stack.empty? ? 0 : stack.last)
        max_length = [max_length, total].max
      else
        prefix = stack.empty? ? 0 : stack.last
        stack << prefix + name.length + 1
      end
    end

    max_length
  end

  alias_method :lengthLongestPath, :length_longest_path
end
