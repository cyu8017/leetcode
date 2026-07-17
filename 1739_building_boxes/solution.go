// LeetCode 1739 - Building Boxes
// https://leetcode.com/problems/building-boxes/

func minimumBoxes(n int) int {
    height := 0
    used := 0
    base := 0
    for used+(height+1)*(height+2)/2 <= n {
        height++
        layer := height * (height + 1) / 2
        used += layer
        base += height
    }
    extra := 0
    for used < n {
        extra++
        used += extra
    }
    return base + extra
}
