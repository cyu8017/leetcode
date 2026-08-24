# LeetCode 0763 - Partition Labels
# https://leetcode.com/problems/partition-labels/

# @param {String} s
# @return {Integer[]}
def partition_labels(s)
  last = {}
  s.chars.each_with_index { |ch, i| last[ch] = i }
  start = 0
  finish = 0
  answer = []
  s.chars.each_with_index do |ch, i|
    finish = [finish, last[ch]].max
    if i == finish
      answer << finish - start + 1
      start = i + 1
    end
  end
  answer
end
