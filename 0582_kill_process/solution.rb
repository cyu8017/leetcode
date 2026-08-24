# LeetCode 0582 - Kill Process
# https://leetcode.com/problems/kill-process/

# @param {Integer[]} pid
# @param {Integer[]} ppid
# @param {Integer} kill
# @return {Integer[]}
def kill_process(pid, ppid, kill)
  children = Hash.new { |h, k| h[k] = [] }
  pid.zip(ppid).each { |child, parent| children[parent] << child }

  result = []
  queue = [kill]
  until queue.empty?
    process = queue.shift
    result << process
    queue.concat(children[process])
  end
  result
end
