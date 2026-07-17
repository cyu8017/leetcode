// LeetCode 1797 - Design Authentication Manager
// https://leetcode.com/problems/design-authentication-manager/

type AuthenticationManager struct {
	ttl    int
	tokens map[string]int
}

func Constructor(timeToLive int) AuthenticationManager {
	return AuthenticationManager{ttl: timeToLive, tokens: make(map[string]int)}
}

func (m *AuthenticationManager) Generate(tokenId string, currentTime int) {
	m.tokens[tokenId] = currentTime + m.ttl
}

func (m *AuthenticationManager) Renew(tokenId string, currentTime int) {
	if exp, ok := m.tokens[tokenId]; ok && exp > currentTime {
		m.tokens[tokenId] = currentTime + m.ttl
	}
}

func (m *AuthenticationManager) CountUnexpiredTokens(currentTime int) int {
	count := 0
	for _, exp := range m.tokens {
		if exp > currentTime {
			count++
		}
	}
	return count
}
