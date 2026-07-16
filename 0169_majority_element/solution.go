// LeetCode 0169 - Majority Element
func majorityElement(nums []int) int {
    candidate, count := 0, 0
    for _, n := range nums {
        if count == 0 { candidate = n }
        if n == candidate { count++ } else { count-- }
    }
    return candidate
}