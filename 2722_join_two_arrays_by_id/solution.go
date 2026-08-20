// LeetCode 2722 - Join Two Arrays by ID
// https://leetcode.com/problems/join-two-arrays-by-id/


import "sort"

func join(arr1, arr2 []map[string]interface{}) []map[string]interface{} {
	m := map[int]map[string]interface{}{}
	getID := func(o map[string]interface{}) int {
		switch v := o["id"].(type) {
		case int:
			return v
		case float64:
			return int(v)
		default:
			return 0
		}
	}
	for _, o := range arr1 {
		id := getID(o)
		cp := map[string]interface{}{}
		for k, v := range o {
			cp[k] = v
		}
		m[id] = cp
	}
	for _, o := range arr2 {
		id := getID(o)
		if cur, ok := m[id]; ok {
			for k, v := range o {
				cur[k] = v
			}
		} else {
			cp := map[string]interface{}{}
			for k, v := range o {
				cp[k] = v
			}
			m[id] = cp
		}
	}
	ids := []int{}
	for id := range m {
		ids = append(ids, id)
	}
	sort.Ints(ids)
	ans := []map[string]interface{}{}
	for _, id := range ids {
		ans = append(ans, m[id])
	}
	return ans
}
