// LeetCode 1792 - Maximum Average Pass Ratio
// https://leetcode.com/problems/maximum-average-pass-ratio/

func maxAverageRatio(classes [][]int, extraStudents int) float64 {
	gain := func(p, t float64) float64 {
		return (p+1)/(t+1) - p/t
	}
	heap := make([][3]float64, len(classes))
	for i, cls := range classes {
		p := float64(cls[0])
		t := float64(cls[1])
		heap[i] = [3]float64{gain(p, t), p, t}
	}
	siftDown := func(i int) {
		n := len(heap)
		for {
			largest := i
			l := 2*i + 1
			r := 2*i + 2
			if l < n && heap[l][0] > heap[largest][0] {
				largest = l
			}
			if r < n && heap[r][0] > heap[largest][0] {
				largest = r
			}
			if largest == i {
				break
			}
			heap[i], heap[largest] = heap[largest], heap[i]
			i = largest
		}
	}
	for i := len(heap)/2 - 1; i >= 0; i-- {
		siftDown(i)
	}
	for k := 0; k < extraStudents; k++ {
		p := heap[0][1] + 1
		t := heap[0][2] + 1
		heap[0] = [3]float64{gain(p, t), p, t}
		siftDown(0)
	}
	total := 0.0
	for _, entry := range heap {
		total += entry[1] / entry[2]
	}
	return total / float64(len(classes))
}
