// LeetCode 1713 - Minimum Operations to Make a Subsequence
// https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/

func minOperations(target []int, arr []int) int {
    pos := make(map[int]int, len(target))
    for i, value := range target {
        pos[value] = i
    }
    lis := []int{}
    for _, value := range arr {
        idx, ok := pos[value]
        if !ok {
            continue
        }
        lo, hi := 0, len(lis)
        for lo < hi {
            mid := (lo + hi) / 2
            if lis[mid] < idx {
                lo = mid + 1
            } else {
                hi = mid
            }
        }
        if lo == len(lis) {
            lis = append(lis, idx)
        } else {
            lis[lo] = idx
        }
    }
    return len(target) - len(lis)
}
