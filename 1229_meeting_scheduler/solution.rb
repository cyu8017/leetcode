# LeetCode 1229 - Meeting Scheduler
# https://leetcode.com/problems/meeting-scheduler/

# @param {Integer[][]} slots1
# @param {Integer[][]} slots2
# @param {Integer} duration
# @return {Integer[]}
def min_available_duration(slots1, slots2, duration)
  slots1 = slots1.sort
  slots2 = slots2.sort
  i = j = 0
  while i < slots1.length && j < slots2.length
    start = [slots1[i][0], slots2[j][0]].max
    finish = [slots1[i][1], slots2[j][1]].min
    return [start, start + duration] if finish - start >= duration
    if slots1[i][1] < slots2[j][1]
      i += 1
    else
      j += 1
    end
  end
  []
end
