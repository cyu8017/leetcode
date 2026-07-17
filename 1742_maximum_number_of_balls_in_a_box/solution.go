// LeetCode 1742 - Maximum Number of Balls in a Box
// https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

func countBalls(lowLimit int, highLimit int) int {
    counts := make(map[int]int)
    for value := lowLimit; value <= highLimit; value++ {
        box := 0
        for v := value; v > 0; v /= 10 {
            box += v % 10
        }
        counts[box]++
    }
    max := 0
    for _, count := range counts {
        if count > max {
            max = count
        }
    }
    return max
}
