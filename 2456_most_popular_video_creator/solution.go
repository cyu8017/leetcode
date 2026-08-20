// LeetCode 2456 - Most Popular Video Creator
// https://leetcode.com/problems/most-popular-video-creator/

func mostPopularCreator(creators []string, ids []string, views []int) [][]string {
	type info struct {
		total int64
		bestID string
		bestViews int
	}
	mp := map[string]*info{}
	var maxTotal int64
	for i, c := range creators {
		if mp[c] == nil {
			mp[c] = &info{bestID: ids[i], bestViews: views[i]}
		}
		mp[c].total += int64(views[i])
		if views[i] > mp[c].bestViews || (views[i] == mp[c].bestViews && ids[i] < mp[c].bestID) {
			mp[c].bestViews = views[i]
			mp[c].bestID = ids[i]
		}
		if mp[c].total > maxTotal {
			maxTotal = mp[c].total
		}
	}
	ans := [][]string{}
	for c, inf := range mp {
		if inf.total == maxTotal {
			ans = append(ans, []string{c, inf.bestID})
		}
	}
	return ans
}
