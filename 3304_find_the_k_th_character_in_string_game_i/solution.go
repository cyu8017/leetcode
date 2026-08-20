// LeetCode 3304 - Find the K-th Character in String Game I
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

func kthCharacter(k int) byte {
	s := []byte{'a'}
	for len(s) < k {
		n := len(s)
		for i := 0; i < n; i++ {
			s = append(s, 'a'+((s[i]-'a'+1)%26))
		}
	}
	return s[k-1]
}
