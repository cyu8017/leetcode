# LeetCode 2244 - Minimum Rounds to Complete All Tasks
# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

# @param {Integer[]} tasks
# @return {Integer}
def minimum_rounds(tasks)
  freq = Hash.new(0)
  tasks.each { |t| freq[t] += 1 }
  ans = 0
  freq.each_value do |c|
    return -1 if c == 1

    ans += (c + 2) / 3
  end
  ans
end
