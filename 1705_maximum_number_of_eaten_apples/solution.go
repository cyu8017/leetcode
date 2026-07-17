// LeetCode 1705 - Maximum Number of Eaten Apples
// https://leetcode.com/problems/maximum-number-of-eaten-apples/

func eatenApples(apples []int, days []int) int {
	heap := [][2]int{}

	push := func(item [2]int) {
		heap = append(heap, item)
		i := len(heap) - 1
		for i > 0 {
			parent := (i - 1) / 2
			if heap[parent][0] <= heap[i][0] {
				break
			}
			heap[parent], heap[i] = heap[i], heap[parent]
			i = parent
		}
	}

	pop := func() [2]int {
		top := heap[0]
		heap[0] = heap[len(heap)-1]
		heap = heap[:len(heap)-1]
		i := 0
		for {
			smallest := i
			left, right := 2*i+1, 2*i+2
			if left < len(heap) && heap[left][0] < heap[smallest][0] {
				smallest = left
			}
			if right < len(heap) && heap[right][0] < heap[smallest][0] {
				smallest = right
			}
			if smallest == i {
				break
			}
			heap[smallest], heap[i] = heap[i], heap[smallest]
			i = smallest
		}
		return top
	}

	n := len(apples)
	day, eaten := 0, 0
	for day < n || len(heap) > 0 {
		if day < n && apples[day] > 0 {
			push([2]int{day + days[day], apples[day]})
		}
		for len(heap) > 0 && heap[0][0] <= day {
			pop()
		}
		if len(heap) > 0 {
			top := pop()
			eaten++
			if top[1] > 1 {
				push([2]int{top[0], top[1] - 1})
			}
		}
		day++
	}
	return eaten
}
