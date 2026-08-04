// LeetCode 1507 - Reformat Date
// https://leetcode.com/problems/reformat-date/

import "fmt"
import "strconv"
import "strings"

func reformatDate(date string) string {
	months := []string{"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}
	parts := strings.Fields(date)
	day, _ := strconv.Atoi(parts[0][:len(parts[0])-2])
	month := 0
	for i, m := range months {
		if m == parts[1] {
			month = i + 1
			break
		}
	}
	return fmt.Sprintf("%s-%02d-%02d", parts[2], month, day)
}
