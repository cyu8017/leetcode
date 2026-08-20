// LeetCode 0676 - Implement Magic Dictionary
// https://leetcode.com/problems/implement-magic-dictionary/

type MagicDictionary struct {
	words []string
}

func Constructor() MagicDictionary {
	return MagicDictionary{}
}

func (m *MagicDictionary) BuildDict(dictionary []string) {
	m.words = dictionary
}

func (m *MagicDictionary) Search(searchWord string) bool {
	for _, word := range m.words {
		if len(word) != len(searchWord) {
			continue
		}
		diff := 0
		for i := 0; i < len(word); i++ {
			if word[i] != searchWord[i] {
				diff++
			}
		}
		if diff == 1 {
			return true
		}
	}
	return false
}
