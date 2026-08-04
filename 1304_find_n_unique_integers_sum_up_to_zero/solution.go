// LeetCode 1304 - Find N Unique Integers Sum up to Zero
// https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

func sumZero(n int) []int {
	answer := make([]int, 0, n)
	for value := 1; value <= n/2; value++ {
		answer = append(answer, -value, value)
	}
	if n%2 == 1 {
		answer = append(answer, 0)
	}
	return answer
}
