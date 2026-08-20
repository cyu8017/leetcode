// LeetCode 0929 - Unique Email Addresses
// https://leetcode.com/problems/unique-email-addresses/

import "strings"

func numUniqueEmails(emails []string) int {
	normalized := map[string]bool{}
	for _, email := range emails {
		parts := strings.Split(email, "@")
		local, domain := parts[0], parts[1]
		if idx := strings.IndexByte(local, '+'); idx >= 0 {
			local = local[:idx]
		}
		local = strings.ReplaceAll(local, ".", "")
		normalized[local+"@"+domain] = true
	}
	return len(normalized)
}
