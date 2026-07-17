// LeetCode 1717 - Maximum Score From Removing Substrings
// https://leetcode.com/problems/maximum-score-from-removing-substrings/

func maximumGain(s string, x int, y int) int {
    remove := func(text string, open, close byte, score int) (string, int) {
        stack := make([]byte, 0, len(text))
        gained := 0
        for i := 0; i < len(text); i++ {
            ch := text[i]
            if len(stack) > 0 && stack[len(stack)-1] == open && ch == close {
                stack = stack[:len(stack)-1]
                gained += score
            } else {
                stack = append(stack, ch)
            }
        }
        return string(stack), gained
    }

    var rest string
    var first, second int
    if x >= y {
        rest, first = remove(s, 'a', 'b', x)
        _, second = remove(rest, 'b', 'a', y)
    } else {
        rest, first = remove(s, 'b', 'a', y)
        _, second = remove(rest, 'a', 'b', x)
    }
    return first + second
}
