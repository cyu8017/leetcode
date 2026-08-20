// LeetCode 3267 - Count Almost Equal Pairs II
// https://leetcode.com/problems/count-almost-equal-pairs-ii/

func countPairs(nums []int) int {
	ans := 0
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			if almostEqual3267(nums[i], nums[j]) {
				ans++
			}
		}
	}
	return ans
}

func almostEqual3267(a, b int) bool {
	sa, sb := padNum(a), padNum(b)
	for len(sa) < len(sb) {
		sa = "0" + sa
	}
	for len(sb) < len(sa) {
		sb = "0" + sb
	}
	if sa == sb {
		return true
	}
	// try up to 2 swaps on sa to match sb
	return canWithSwaps(sa, sb, 2)
}

func padNum(x int) string {
	if x == 0 {
		return "0"
	}
	var b []byte
	for x > 0 {
		b = append([]byte{byte('0' + x%10)}, b...)
		x /= 10
	}
	return string(b)
}

func canWithSwaps(sa, sb string, maxSwap int) bool {
	bsa := []byte(sa)
	var dfs func(int, int) bool
	dfs = func(start, left int) bool {
		if string(bsa) == sb {
			return true
		}
		if left == 0 {
			return false
		}
		for i := start; i < len(bsa); i++ {
			if bsa[i] == sb[i] {
				continue
			}
			for j := i + 1; j < len(bsa); j++ {
				if bsa[j] == sb[i] {
					bsa[i], bsa[j] = bsa[j], bsa[i]
					if dfs(i+1, left-1) {
						return true
					}
					bsa[i], bsa[j] = bsa[j], bsa[i]
				}
			}
			return false
		}
		return string(bsa) == sb
	}
	return dfs(0, maxSwap)
}
