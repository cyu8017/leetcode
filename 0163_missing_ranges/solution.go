// LeetCode 0163 - Missing Ranges
func findMissingRanges(nums []int, lower int, upper int) [][]int {
    result := [][]int{}
    previous := int64(lower) - 1
    for i := 0; i <= len(nums); i++ {
        current := int64(upper) + 1
        if i < len(nums) { current = int64(nums[i]) }
        if current-previous >= 2 { result = append(result, []int{int(previous + 1), int(current - 1)}) }
        previous = current
    }
    return result
}