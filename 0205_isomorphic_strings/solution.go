// LeetCode 0205 - Isomorphic Strings
func isIsomorphic(s string, t string) bool { mapS, mapT := make(map[byte]byte), make(map[byte]byte); if len(s) != len(t) { return false }; for i := range s { a, b := s[i], t[i]; if mapped, ok := mapS[a]; ok && mapped != b { return false }; if mapped, ok := mapT[b]; ok && mapped != a { return false }; mapS[a], mapT[b] = b, a }; return true }
