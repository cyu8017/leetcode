// LeetCode 0164 - Maximum Gap
func maximumGap(nums []int) int {
    if len(nums) < 2 { return 0 }
    low, high := nums[0], nums[0]
    for _, n := range nums { if n < low { low = n }; if n > high { high = n } }
    if low == high { return 0 }
    size := (high-low)/(len(nums)-1); if size < 1 { size = 1 }
    count := (high-low)/size + 1
    mins, maxs, used := make([]int, count), make([]int, count), make([]bool, count)
    for i := range mins { mins[i] = int(^uint(0) >> 1); maxs[i] = -mins[i] - 1 }
    for _, n := range nums {
        i := (n-low)/size
        if n < mins[i] { mins[i] = n }; if n > maxs[i] { maxs[i] = n }; used[i] = true
    }
    best, previous := 0, low
    for i := range used { if used[i] { if mins[i]-previous > best { best = mins[i]-previous }; previous = maxs[i] } }
    return best
}