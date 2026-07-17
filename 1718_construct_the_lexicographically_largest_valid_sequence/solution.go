// LeetCode 1718 - Construct the Lexicographically Largest Valid Sequence
// https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

func constructDistancedSequence(n int) []int {
    ans := make([]int, 2*n-1)
    used := make([]bool, n+1)

    var backtrack func(i int) bool
    backtrack = func(i int) bool {
        for i < len(ans) && ans[i] != 0 {
            i++
        }
        if i == len(ans) {
            return true
        }
        for value := n; value >= 1; value-- {
            if used[value] {
                continue
            }
            if value == 1 {
                ans[i] = 1
                used[1] = true
                if backtrack(i + 1) {
                    return true
                }
                used[1] = false
                ans[i] = 0
            } else {
                j := i + value
                if j < len(ans) && ans[j] == 0 {
                    ans[i], ans[j] = value, value
                    used[value] = true
                    if backtrack(i + 1) {
                        return true
                    }
                    used[value] = false
                    ans[i], ans[j] = 0, 0
                }
            }
        }
        return false
    }

    backtrack(0)
    return ans
}
