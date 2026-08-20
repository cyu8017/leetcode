// LeetCode 0751 - IP to CIDR
// https://leetcode.com/problems/ip-to-cidr/

import (
	"fmt"
	"strconv"
	"strings"
)

func ipToCIDR(ip string, n int) []string {
	ipToInt := func(value string) int {
		result := 0
		for _, part := range strings.Split(value, ".") {
			v, _ := strconv.Atoi(part)
			result = result*256 + v
		}
		return result
	}
	intToIP := func(value int) string {
		return fmt.Sprintf("%d.%d.%d.%d", (value>>24)&255, (value>>16)&255, (value>>8)&255, value&255)
	}
	start := ipToInt(ip)
	answer := []string{}
	for n > 0 {
		lowbit := 1 << 32
		if start != 0 {
			lowbit = start & -start
		}
		for lowbit > n {
			lowbit >>= 1
		}
		mask := 32
		lb := lowbit
		for lb > 1 {
			lb >>= 1
			mask--
		}
		answer = append(answer, fmt.Sprintf("%s/%d", intToIP(start), mask))
		start += lowbit
		n -= lowbit
	}
	return answer
}
