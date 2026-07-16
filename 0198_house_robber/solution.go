// LeetCode 0198 - House Robber
// https://leetcode.com/problems/house-robber/

func rob(nums []int) int {
    previousTwo, previousOne := 0, 0
    for _, value := range nums {
        current := previousOne
        if previousTwo+value > current {
            current = previousTwo + value
        }
        previousTwo, previousOne = previousOne, current
    }
    return previousOne
}
