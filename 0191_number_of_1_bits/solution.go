// LeetCode 0191 - Number of 1 Bits
// https://leetcode.com/problems/number-of-1-bits/

func hammingWeight(n uint32) int {
    count := 0
    for n != 0 {
        n &= n - 1
        count++
    }
    return count
}
