// LeetCode 1604 - Alert Using Same Key-Card Three or More Times in a One Hour Period
// https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/

import (
	"sort"
	"strconv"
	"strings"
)

func alertNames(keyName []string, keyTime []string) []string {
	times := map[string][]int{}
	for i, name := range keyName {
		parts := strings.Split(keyTime[i], ":")
		h, _ := strconv.Atoi(parts[0])
		m, _ := strconv.Atoi(parts[1])
		times[name] = append(times[name], h*60+m)
	}
	ans := []string{}
	for name, a := range times {
		sort.Ints(a)
		for i := 0; i+2 < len(a); i++ {
			if a[i+2]-a[i] <= 60 {
				ans = append(ans, name)
				break
			}
		}
	}
	sort.Strings(ans)
	return ans
}
