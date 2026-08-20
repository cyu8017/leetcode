// LeetCode 3280 - Convert Date to Binary
// https://leetcode.com/problems/convert-date-to-binary/

import "fmt"
import "strconv"
import "strings"

func convertDateToBinary(date string) string {
	parts := strings.Split(date, "-")
	out := make([]string, 3)
	for i, p := range parts {
		v, _ := strconv.Atoi(p)
		out[i] = fmt.Sprintf("%b", v)
	}
	return strings.Join(out, "-")
}
