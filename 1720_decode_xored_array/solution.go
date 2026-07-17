// LeetCode 1720 - Decode XORed Array
// https://leetcode.com/problems/decode-xored-array/

func decode(encoded []int, first int) []int {
    ans := make([]int, 0, len(encoded)+1)
    ans = append(ans, first)
    for _, value := range encoded {
        ans = append(ans, ans[len(ans)-1]^value)
    }
    return ans
}
