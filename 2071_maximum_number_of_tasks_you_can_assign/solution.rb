# LeetCode 2071 - Maximum Number of Tasks You Can Assign
# https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/

# @param {Integer[]} tasks
# @param {Integer[]} workers
# @param {Integer} pills
# @param {Integer} strength
# @return {Integer}
def max_task_assign(tasks, workers, pills, strength)
  tasks.sort!
  workers.sort!

  remove = lambda do |ws, x|
    ws[x] -= 1
    ws.delete(x) if ws[x].zero?
  end

  can = lambda do |k|
    return true if k.zero?

    ws = Hash.new(0)
    workers[workers.length - k..].each { |w| ws[w] += 1 }
    p = pills
    (k - 1).downto(0) do |i|
      task = tasks[i]
      ks = ws.keys.sort
      strongest = ks[-1]
      if strongest >= task
        remove.call(ws, strongest)
        next
      end
      return false if p.zero?

      need = task - strength
      found = ks.find { |key| key >= need }
      return false if found.nil?

      remove.call(ws, found)
      p -= 1
    end
    true
  end

  lo = 0
  hi = [tasks.length, workers.length].min
  while lo < hi
    mid = (lo + hi + 1) >> 1
    if can.call(mid)
      lo = mid
    else
      hi = mid - 1
    end
  end
  lo
end
