// LeetCode 3443 - Maximum Manhattan Distance After K Changes
// https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/

func maxDistance(s string, k int) int {
	ans := 0
	lat, lon := 0, 0
	for i, c := range s {
		switch c {
		case 'N':
			lat++
		case 'S':
			lat--
		case 'E':
			lon++
		case 'W':
			lon--
		}
		md := lat
		if md < 0 {
			md = -md
		}
		if lon < 0 {
			md += -lon
		} else {
			md += lon
		}
		steps := i + 1
		// with up to k changes, max distance is min(steps, md+2*k)
		cur := md + 2*k
		if cur > steps {
			cur = steps
		}
		if cur > ans {
			ans = cur
		}
	}
	return ans
}
