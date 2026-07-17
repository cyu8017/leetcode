// LeetCode 1882 - Process Tasks Using Servers
// https://leetcode.com/problems/process-tasks-using-servers/

import "container/heap"

type availableServer struct {
	weight int
	index  int
}

type availableHeap []availableServer

func (servers availableHeap) Len() int           { return len(servers) }
func (servers availableHeap) Less(i, j int) bool { return servers[i].weight < servers[j].weight || (servers[i].weight == servers[j].weight && servers[i].index < servers[j].index) }
func (servers availableHeap) Swap(i, j int)      { servers[i], servers[j] = servers[j], servers[i] }
func (servers *availableHeap) Push(value interface{}) {
	*servers = append(*servers, value.(availableServer))
}
func (servers *availableHeap) Pop() interface{} {
	old := *servers
	item := old[len(old)-1]
	*servers = old[:len(old)-1]
	return item
}

type busyServer struct {
	finishTime int
	weight     int
	index      int
}

type busyHeap []busyServer

func (servers busyHeap) Len() int           { return len(servers) }
func (servers busyHeap) Less(i, j int) bool { return servers[i].finishTime < servers[j].finishTime }
func (servers busyHeap) Swap(i, j int)      { servers[i], servers[j] = servers[j], servers[i] }
func (servers *busyHeap) Push(value interface{}) {
	*servers = append(*servers, value.(busyServer))
}
func (servers *busyHeap) Pop() interface{} {
	old := *servers
	item := old[len(old)-1]
	*servers = old[:len(old)-1]
	return item
}

func assignTasks(servers []int, tasks []int) []int {
	available := make(availableHeap, 0, len(servers))
	for index, weight := range servers {
		heap.Push(&available, availableServer{weight: weight, index: index})
	}
	busy := make(busyHeap, 0)
	answer := make([]int, 0, len(tasks))
	time := 0

	releaseFinished := func() {
		for busy.Len() > 0 && busy[0].finishTime <= time {
			server := heap.Pop(&busy).(busyServer)
			heap.Push(&available, availableServer{weight: server.weight, index: server.index})
		}
	}

	for moment, task := range tasks {
		if moment > time {
			time = moment
		}
		releaseFinished()

		for available.Len() == 0 {
			time = busy[0].finishTime
			releaseFinished()
		}

		server := heap.Pop(&available).(availableServer)
		heap.Push(&busy, busyServer{
			finishTime: time + task,
			weight:     server.weight,
			index:      server.index,
		})
		answer = append(answer, server.index)
	}

	return answer
}
