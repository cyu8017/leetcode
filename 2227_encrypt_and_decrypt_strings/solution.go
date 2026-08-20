// LeetCode 2227 - Encrypt and Decrypt Strings
// https://leetcode.com/problems/encrypt-and-decrypt-strings/

type Encrypter struct {
	enc map[byte]string
	cnt map[string]int
}

func Constructor(keys []byte, values []string, dictionary []string) Encrypter {
	enc := map[byte]string{}
	for i, k := range keys {
		enc[k] = values[i]
	}
	e := Encrypter{enc: enc, cnt: map[string]int{}}
	for _, w := range dictionary {
		e.cnt[e.Encrypt(w)]++
	}
	return e
}

func (this *Encrypter) Encrypt(word1 string) string {
	b := make([]byte, 0, len(word1)*2)
	for i := 0; i < len(word1); i++ {
		v, ok := this.enc[word1[i]]
		if !ok {
			return ""
		}
		b = append(b, v...)
	}
	return string(b)
}

func (this *Encrypter) Decrypt(word2 string) int {
	return this.cnt[word2]
}
