# LeetCode 0451 - Sort Characters By Frequency
# https://leetcode.com/problems/sort-characters-by-frequency/

class Solution
  def frequency_sort(s)
    counts = Hash.new(0)
    s.each_char { |ch| counts[ch] += 1 }
    counts
      .sort_by { |ch, count| [-count, ch] }
      .map { |ch, count| ch * count }
      .join
  end

  alias_method :frequencySort, :frequency_sort
end
