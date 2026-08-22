// LeetCode 3408 - Design Task Manager
// https://leetcode.com/problems/design-task-manager/

import "container/heap"

type taskItem struct{ pri, taskId, userId int }
type taskHeap []taskItem

func (h taskHeap) Len() int { return len(h) }
func (h taskHeap) Less(i, j int) bool {
	if h[i].pri == h[j].pri {
		return h[i].taskId > h[j].taskId
	}
	return h[i].pri > h[j].pri
}
func (h taskHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *taskHeap) Push(x interface{}) { *h = append(*h, x.(taskItem)) }
func (h *taskHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type TaskManager struct {
	h    *taskHeap
	pri  map[int]int
	user map[int]int
}

func Constructor(tasks [][]int) TaskManager {
	tm := TaskManager{h: &taskHeap{}, pri: map[int]int{}, user: map[int]int{}}
	for _, t := range tasks {
		tm.Add(t[0], t[1], t[2])
	}
	return tm
}

func (this *TaskManager) Add(userId int, taskId int, priority int) {
	this.pri[taskId] = priority
	this.user[taskId] = userId
	heap.Push(this.h, taskItem{priority, taskId, userId})
}

func (this *TaskManager) Edit(taskId int, newPriority int) {
	this.pri[taskId] = newPriority
	heap.Push(this.h, taskItem{newPriority, taskId, this.user[taskId]})
}

func (this *TaskManager) Rmv(taskId int) {
	delete(this.pri, taskId)
	delete(this.user, taskId)
}

func (this *TaskManager) ExecTop() int {
	for this.h.Len() > 0 {
		top := heap.Pop(this.h).(taskItem)
		if p, ok := this.pri[top.taskId]; ok && p == top.pri && this.user[top.taskId] == top.userId {
			delete(this.pri, top.taskId)
			uid := this.user[top.taskId]
			delete(this.user, top.taskId)
			return uid
		}
	}
	return -1
}
