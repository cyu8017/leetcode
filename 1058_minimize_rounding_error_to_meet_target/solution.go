// LeetCode 1058 - Minimize Rounding Error to Meet Target
// https://leetcode.com/problems/minimize-rounding-error-to-meet-target/

import (
	"fmt"
	"sort"
	"strconv"
)

func minimizeError(prices []string, target int) string {
	floors := 0
	fracs := []float64{}
	for _, p := range prices {
		value, _ := strconv.ParseFloat(p, 64)
		floor := int(value)
		floors += floor
		frac := value - float64(floor)
		if frac > 1e-9 {
			fracs = append(fracs, frac)
		}
	}
	ceilCount := target - floors
	if ceilCount < 0 || ceilCount > len(fracs) {
		return "-1"
	}
	sort.Sort(sort.Reverse(sort.Float64Slice(fracs)))
	error := 0.0
	for i, f := range fracs {
		if i < ceilCount {
			error += 1 - f
		} else {
			error += f
		}
	}
	return fmt.Sprintf("%.3f", error)
}
