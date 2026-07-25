// LeetCode 1687 - Delivering Boxes from Storage to Ports
// https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/

func boxDelivering(boxes [][]int, portsCount, maxBoxes, maxWeight int) int {
	n := len(boxes)
	w := make([]int, n+1)
	changes := make([]int, n+1)
	for i := 1; i <= n; i++ {
		w[i] = w[i-1] + boxes[i-1][1]
		changes[i] = changes[i-1]
		if i > 1 && boxes[i-1][0] != boxes[i-2][0] {
			changes[i]++
		}
	}
	dp := make([]int, n+1)
	q := []int{0}
	for i := 1; i <= n; i++ {
		for len(q) > 0 && (i-q[0] > maxBoxes || w[i]-w[q[0]] > maxWeight) {
			q = q[1:]
		}
		j := q[0]
		dp[i] = dp[j] + changes[i] - changes[j+1] + 2
		if i < n {
			val := dp[i] - changes[i+1]
			for len(q) > 0 && dp[q[len(q)-1]]-changes[q[len(q)-1]+1] >= val {
				q = q[:len(q)-1]
			}
			q = append(q, i)
		}
	}
	return dp[n]
}
