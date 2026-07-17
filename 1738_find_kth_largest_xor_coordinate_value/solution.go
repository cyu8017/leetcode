// LeetCode 1738 - Find Kth Largest XOR Coordinate Value
// https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/

import "sort"

func kthLargestValue(matrix [][]int, k int) int {
    rows, cols := len(matrix), len(matrix[0])
    pref := make([][]int, rows+1)
    for i := range pref {
        pref[i] = make([]int, cols+1)
    }
    values := make([]int, 0, rows*cols)
    for r := 1; r <= rows; r++ {
        for c := 1; c <= cols; c++ {
            pref[r][c] = pref[r-1][c] ^ pref[r][c-1] ^ pref[r-1][c-1] ^ matrix[r-1][c-1]
            values = append(values, pref[r][c])
        }
    }
    sort.Sort(sort.Reverse(sort.IntSlice(values)))
    return values[k-1]
}
