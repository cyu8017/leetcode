// LeetCode 0168 - Excel Sheet Column Title
func convertToTitle(columnNumber int) string {
    result := []byte{}
    for columnNumber > 0 {
        columnNumber--
        result = append(result, byte('A'+columnNumber%26))
        columnNumber /= 26
    }
    for left, right := 0, len(result)-1; left < right; left, right = left+1, right-1 {
        result[left], result[right] = result[right], result[left]
    }
    return string(result)
}