// LeetCode 3860 - Unique Email Groups
// https://leetcode.com/problems/unique-email-groups/

import "strings"

func uniqueEmailGroups(emails []string) int {
	st := make(map[string]struct{})

	for _, email := range emails {
		parts := strings.Split(email, "@")
		local := parts[0]
		domain := parts[1]

		if idx := strings.Index(local, "+"); idx != -1 {
			local = local[:idx]
		}

		local = strings.ReplaceAll(local, ".", "")
		local = strings.ToLower(local)
		domain = strings.ToLower(domain)

		normalized := local + domain
		st[normalized] = struct{}{}
	}

	return len(st)
}
