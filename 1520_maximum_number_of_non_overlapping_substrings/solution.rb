# LeetCode 1520 - Maximum Number of Non-Overlapping Substrings
# https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/

# @param {String} s
# @return {String[]}
def max_num_of_substrings(s)
  first = {}
  last = {}
  s.chars.each_with_index do |ch, i|
    first[ch] = i unless first.key?(ch)
    last[ch] = i
  end
  intervals = []
  s.chars.each_with_index do |ch, i|
    next unless first[ch] == i
    ending = last[ch]
    j = i
    valid = true
    while j <= ending
      if first[s[j]] < i
        valid = false
        break
      end
      ending = [ending, last[s[j]]].max
      j += 1
    end
    intervals << [ending, i] if valid
  end
  intervals.sort!
  answer = []
  previous_end = -1
  intervals.each do |ending, start|
    if start > previous_end
      answer << s[start..ending]
      previous_end = ending
    end
  end
  answer.sort_by(&:length)
end
