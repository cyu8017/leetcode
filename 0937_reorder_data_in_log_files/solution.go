// LeetCode 0937 - Reorder Data in Log Files
// https://leetcode.com/problems/reorder-data-in-log-files/

import (
	"sort"
	"strings"
	"unicode"
)

func reorderLogFiles(logs []string) []string {
	sort.SliceStable(logs, func(i, j int) bool {
		a, b := logs[i], logs[j]
		ai := strings.IndexByte(a, ' ')
		bi := strings.IndexByte(b, ' ')
		arest, brest := a[ai+1:], b[bi+1:]
		aletter := unicode.IsLetter(rune(arest[0]))
		bletter := unicode.IsLetter(rune(brest[0]))
		if aletter && bletter {
			if arest != brest {
				return arest < brest
			}
			return a[:ai] < b[:bi]
		}
		if aletter {
			return true
		}
		if bletter {
			return false
		}
		return false
	})
	return logs
}
