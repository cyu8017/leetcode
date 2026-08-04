// LeetCode 1108 - Defanging an IP Address
// https://leetcode.com/problems/defanging-an-ip-address/

import "strings"

func defangIPaddr(address string) string {
	return strings.ReplaceAll(address, ".", "[.]")
}
