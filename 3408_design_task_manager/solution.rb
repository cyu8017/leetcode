# LeetCode 3408 - Design Task Manager
# https://leetcode.com/problems/design-task-manager/

class TaskManager
  def initialize(tasks)
    @pri = {}
    @user = {}
    @h = []
    tasks.each { |t| add(t[0], t[1], t[2]) }
  end

  def add(user_id, task_id, priority)
    @pri[task_id] = priority
    @user[task_id] = user_id
    @h << [priority, task_id, user_id]
  end

  def edit(task_id, new_priority)
    @pri[task_id] = new_priority
    @h << [new_priority, task_id, @user[task_id]]
  end

  def rmv(task_id)
    @pri.delete(task_id)
    @user.delete(task_id)
  end

  def exec_top
    @h.sort_by! { |a| [a[0], a[1]] }
    until @h.empty?
      top = @h.pop
      p = @pri[top[1]]
      if !p.nil? && p == top[0] && @user[top[1]] == top[2]
        @pri.delete(top[1])
        uid = @user[top[1]]
        @user.delete(top[1])
        return uid
      end
    end
    -1
  end
end
