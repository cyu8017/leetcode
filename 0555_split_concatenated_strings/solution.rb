# LeetCode 0555 - Split Concatenated Strings
# https://leetcode.com/problems/split-concatenated-strings/

# @param {String[]} strs
# @return {String}
def split_looped_string(strs)
  best_forms = strs.map { |s| [s, s.reverse].max }
  answer = ""

  strs.each_with_index do |original, i|
    mid = (best_forms[(i + 1)..] + best_forms[0...i]).join
    [original, original.reverse].each do |candidate|
      candidate.length.times do |cut|
        formed = candidate[cut..] + mid + candidate[0...cut]
        answer = formed if formed > answer
      end
    end
  end

  answer
end
