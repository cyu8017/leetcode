// LeetCode 3750 - Minimum Number Of Flips To Reverse Binary String
// https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/

import "strconv"

func minimumFlips(n int) int {
    s := strconv.FormatInt(int64(n), 2)
    m := len(s)
    cnt := 0
    for i := 0; i < m/2; i++ {
        if s[i] != s[m-i-1] {
            cnt++
        }
    }
    return cnt * 2
}
