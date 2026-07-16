// LeetCode 0208 - Implement Trie (Prefix Tree)
type Trie struct { children [26]*Trie; isWord bool }
func Constructor() Trie { return Trie{} }
func (this *Trie) Insert(word string) { node := this; for i := range word { index := word[i] - 'a'; if node.children[index] == nil { node.children[index] = &Trie{} }; node = node.children[index] }; node.isWord = true }
func (this *Trie) find(text string) *Trie { node := this; for i := range text { node = node.children[text[i]-'a']; if node == nil { return nil } }; return node }
func (this *Trie) Search(word string) bool { node := this.find(word); return node != nil && node.isWord }
func (this *Trie) StartsWith(prefix string) bool { return this.find(prefix) != nil }
