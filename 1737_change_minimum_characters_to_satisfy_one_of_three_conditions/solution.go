// LeetCode 1737 - Change Minimum Characters to Satisfy One of Three Conditions
// https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/

func minCharacters(a string, b string) int {
    var ca, cb [26]int
    for i := 0; i < len(a); i++ {
        ca[a[i]-'a']++
    }
    for i := 0; i < len(b); i++ {
        cb[b[i]-'a']++
    }
    n, m := len(a), len(b)
    maxCount := 0
    for i := 0; i < 26; i++ {
        if ca[i] > maxCount {
            maxCount = ca[i]
        }
        if cb[i] > maxCount {
            maxCount = cb[i]
        }
    }
    ans := n + m - maxCount
    preA, preB := 0, 0
    for code := 0; code < 25; code++ {
        preA += ca[code]
        preB += cb[code]
        if cond := n - preA + preB; cond < ans {
            ans = cond
        }
        if cond := m - preB + preA; cond < ans {
            ans = cond
        }
    }
    return ans
}
