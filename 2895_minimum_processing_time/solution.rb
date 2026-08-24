# LeetCode 2895 - Minimum Processing Time
# https://leetcode.com/problems/minimum-processing-time/

# @param {Integer[]} processor_time
# @param {Integer[]} tasks
# @return {Integer}
def min_processing_time(processor_time, tasks)
  processor_time = processor_time.sort
  tasks = tasks.sort.reverse
  ans = 0
  processor_time.each_with_index do |pt, i|
    fin = pt + tasks[i * 4]
    ans = fin if fin > ans
  end
  ans
end
