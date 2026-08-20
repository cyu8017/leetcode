// LeetCode 0800 - Similar RGB Color
// https://leetcode.com/problems/similar-rgb-color/

import "fmt"

func similarRGB(color string) string {
	closest := func(component string) string {
		var value int
		fmt.Sscanf(component, "%x", &value)
		rounded := (value + 8) / 17
		return fmt.Sprintf("%x%x", rounded, rounded)
	}
	return "#" + closest(color[1:3]) + closest(color[3:5]) + closest(color[5:7])
}
