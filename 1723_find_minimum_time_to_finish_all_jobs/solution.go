// LeetCode 1723 - Find Minimum Time to Finish All Jobs
// https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/

import "sort"

func minimumTimeRequired(jobs []int, k int) int {
    sort.Sort(sort.Reverse(sort.IntSlice(jobs)))
    loads := make([]int, k)
    best := 0
    for _, job := range jobs {
        best += job
    }

    var backtrack func(i int)
    backtrack = func(i int) {
        if i == len(jobs) {
            max := 0
            for _, load := range loads {
                if load > max {
                    max = load
                }
            }
            if max < best {
                best = max
            }
            return
        }
        seen := make(map[int]bool)
        for worker := 0; worker < k; worker++ {
            if seen[loads[worker]] {
                continue
            }
            if loads[worker]+jobs[i] >= best {
                continue
            }
            seen[loads[worker]] = true
            loads[worker] += jobs[i]
            backtrack(i + 1)
            loads[worker] -= jobs[i]
            if loads[worker] == 0 {
                break
            }
        }
    }

    backtrack(0)
    return best
}
