// LeetCode 1776 - Car Fleet II
// https://leetcode.com/problems/car-fleet-ii/

func getCollisionTimes(cars [][]int) []float64 {
    n := len(cars)
    ans := make([]float64, n)
    for i := range ans {
        ans[i] = -1.0
    }
    stack := make([]int, 0, n)
    for i := n - 1; i >= 0; i-- {
        pos, speed := cars[i][0], cars[i][1]
        for len(stack) > 0 {
            j := stack[len(stack)-1]
            if speed <= cars[j][1] {
                stack = stack[:len(stack)-1]
                continue
            }
            t := float64(cars[j][0]-pos) / float64(speed-cars[j][1])
            if ans[j] < 0 || t <= ans[j] {
                ans[i] = t
                break
            }
            stack = stack[:len(stack)-1]
        }
        stack = append(stack, i)
    }
    return ans
}
