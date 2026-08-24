# LeetCode 2590 - Design a Todo List
# https://leetcode.com/problems/design-a-todo-list/

class TodoList
  def initialize
    @next_id = 1
    @tasks = {}
    @users = {}
  end

  def add_task(user_id, task_description, due_date, tags)
    tid = @next_id
    @next_id += 1
    @tasks[tid] = {
      id: tid,
      description: task_description,
      due_date: due_date,
      user_id: user_id,
      tags: tags.to_h { |t| [t, true] },
      done: false
    }
    @users[user_id] ||= []
    @users[user_id] << tid
    tid
  end

  def get_all_tasks(user_id)
    return [] unless @users.key?(user_id)

    ids = @users[user_id].dup
    ids.sort_by! { |i| @tasks[i][:due_date] }
    ans = []
    ids.each do |tid|
      ans << @tasks[tid][:description] unless @tasks[tid][:done]
    end
    ans
  end

  def get_tasks_for_tag(user_id, tag)
    return [] unless @users.key?(user_id)

    ids = @users[user_id].dup
    ids.sort_by! { |i| @tasks[i][:due_date] }
    ans = []
    ids.each do |tid|
      tk = @tasks[tid]
      ans << tk[:description] if !tk[:done] && tk[:tags][tag]
    end
    ans
  end

  def complete_task(user_id, task_id)
    tk = @tasks[task_id]
    return if tk.nil? || tk[:user_id] != user_id || tk[:done]

    tk[:done] = true
    nil
  end
end
