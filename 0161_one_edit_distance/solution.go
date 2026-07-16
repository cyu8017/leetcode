// LeetCode 0161 - One Edit Distance
func isOneEditDistance(s string, t string) bool {
    if len(s) > len(t) { return isOneEditDistance(t, s) }
    if len(t)-len(s) > 1 || s == t { return false }
    i := 0
    for i < len(s) && s[i] == t[i] { i++ }
    if len(s) == len(t) { return s[i+1:] == t[i+1:] }
    return s[i:] == t[i+1:]
}