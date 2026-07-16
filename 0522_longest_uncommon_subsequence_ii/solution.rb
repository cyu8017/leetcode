# LeetCode 0522 - Longest Uncommon Subsequence II
# https://leetcode.com/problems/longest-uncommon-subsequence-ii/

class Solution
  def find_luslength(strs)
    result = -1
    strs.each_with_index do |candidate, i|
      next if strs.each_with_index.any? { |other, j| i != j && subsequence?(candidate, other) }

      result = [result, candidate.length].max
    end
    result
  end

  alias_method :findLUSlength, :find_luslength

  private

  def subsequence?(target, source)
    index = 0
    source.each_char do |char|
      index += 1 if index < target.length && target[index] == char
    end
    index == target.length
  end
end
