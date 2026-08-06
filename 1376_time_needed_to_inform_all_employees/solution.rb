# LeetCode 1376 - Time Needed To Inform All Employees
# https://leetcode.com/problems/time-needed-to-inform-all-employees/

def num_of_minutes(n, head_id, manager, inform_time)
  children = Array.new(n) { [] }
  manager.each_with_index { |p, i| children[p] << i if p != -1 }
  dfs = lambda do |u|
    kids = children[u]
    inform_time[u] + (kids.empty? ? 0 : kids.map { |v| dfs.call(v) }.max)
  end
  dfs.call(head_id)
end
