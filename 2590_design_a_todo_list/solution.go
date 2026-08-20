// LeetCode 2590 - Design a Todo List
// https://leetcode.com/problems/design-a-todo-list/


import "sort"
import "strings"

type task struct {
	id          int
	description string
	dueDate     int
	tags        map[string]bool
	done        bool
	userId      int
}

type TodoList struct {
	nextID int
	tasks  map[int]*task
	users  map[int][]int
}

func Constructor() TodoList {
	return TodoList{nextID: 1, tasks: map[int]*task{}, users: map[int][]int{}}
}

func (t *TodoList) AddTask(userId int, taskDescription string, dueDate int, tags []string) int {
	id := t.nextID
	t.nextID++
	tg := map[string]bool{}
	for _, x := range tags {
		tg[x] = true
	}
	tk := &task{id: id, description: taskDescription, dueDate: dueDate, tags: tg, userId: userId}
	t.tasks[id] = tk
	t.users[userId] = append(t.users[userId], id)
	return id
}

func (t *TodoList) GetAllTasks(userId int) []string {
	ids := append([]int(nil), t.users[userId]...)
	sort.Slice(ids, func(i, j int) bool {
		return t.tasks[ids[i]].dueDate < t.tasks[ids[j]].dueDate
	})
	ans := []string{}
	for _, id := range ids {
		tk := t.tasks[id]
		if !tk.done {
			ans = append(ans, tk.description)
		}
	}
	return ans
}

func (t *TodoList) GetTasksForTag(userId int, tag string) []string {
	ids := append([]int(nil), t.users[userId]...)
	sort.Slice(ids, func(i, j int) bool {
		return t.tasks[ids[i]].dueDate < t.tasks[ids[j]].dueDate
	})
	ans := []string{}
	for _, id := range ids {
		tk := t.tasks[id]
		if !tk.done && tk.tags[tag] {
			ans = append(ans, tk.description)
		}
	}
	return ans
}

func (t *TodoList) CompleteTask(userId int, taskId int) {
	tk, ok := t.tasks[taskId]
	if !ok || tk.userId != userId || tk.done {
		return
	}
	tk.done = true
	_ = strings.TrimSpace
}
