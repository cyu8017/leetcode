// LeetCode 1257 - Smallest Common Region
// https://leetcode.com/problems/smallest-common-region/

func findSmallestRegion(regions [][]string, region1 string, region2 string) string {
	parent := map[string]string{}
	for _, group := range regions {
		for _, child := range group[1:] {
			parent[child] = group[0]
		}
	}
	ancestors := map[string]bool{}
	for region1 != "" {
		ancestors[region1] = true
		region1 = parent[region1]
	}
	for !ancestors[region2] {
		region2 = parent[region2]
	}
	return region2
}
