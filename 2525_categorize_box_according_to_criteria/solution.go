// LeetCode 2525 - Categorize Box According to Criteria
// https://leetcode.com/problems/categorize-box-according-to-criteria/

func categorizeBox(length int, width int, height int, mass int) string {
	bulky := length >= 10000 || width >= 10000 || height >= 10000 ||
		int64(length)*int64(width)*int64(height) >= 1000000000
	heavy := mass >= 100
	if bulky && heavy {
		return "Both"
	}
	if bulky {
		return "Bulky"
	}
	if heavy {
		return "Heavy"
	}
	return "Neither"
}
