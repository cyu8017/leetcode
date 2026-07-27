# LeetCode 1665 - Minimum Initial Energy to Finish Tasks
# https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/

# @param {Integer[][]} tasks
# @return {Integer}
def minimum_effort(tasks)
  tasks = tasks.sort_by { |t| -(t[1] - t[0]) }
  energy = 0
  spent = 0
  tasks.each do |cost, minimum|
    energy = [energy, spent + minimum].max
    spent += cost
  end
  energy
end
