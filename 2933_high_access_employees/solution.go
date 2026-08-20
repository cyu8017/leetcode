// LeetCode 2933 - High-Access Employees
// https://leetcode.com/problems/high-access-employees/

import "sort"

func findHighAccessEmployees(accessTimes [][]string) []string {
	m := map[string][]int{}
	for _, a := range accessTimes {
		name, t := a[0], a[1]
		hh := int(t[0]-'0')*10 + int(t[1]-'0')
		mm := int(t[2]-'0')*10 + int(t[3]-'0')
		m[name] = append(m[name], hh*60+mm)
	}
	ans := []string{}
	for name, times := range m {
		sort.Ints(times)
		for i := 0; i+2 < len(times); i++ {
			if times[i+2]-times[i] < 60 {
				ans = append(ans, name)
				break
			}
		}
	}
	sort.Strings(ans)
	return ans
}
