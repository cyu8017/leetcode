# LeetCode 0893 - Groups of Special-Equivalent Strings
# https://leetcode.com/problems/groups-of-special-equivalent-strings/

# @param {String[]} words
# @return {Integer}
def num_special_equiv_groups(words)
  groups = {}
  words.each do |w|
    even = w.chars.each_slice(2).map(&:first).sort.join
    odd = w.chars.each_slice(2).map { |pair| pair[1] }.compact.sort.join
    groups[[even, odd]] = true
  end
  groups.length
end
