// LeetCode 0208 - Implement Trie (Prefix Tree)
#include <stdbool.h>
#include <stdlib.h>
typedef struct Trie { struct Trie* children[26]; bool isWord; } Trie;
Trie* trieCreate(void) { return calloc(1, sizeof(Trie)); }
void trieInsert(Trie* obj, char* word) { for (; *word; ++word) { int index = *word - 'a'; if (!obj->children[index]) obj->children[index] = trieCreate(); obj = obj->children[index]; } obj->isWord = true; }
static Trie* trieFind(Trie* obj, char* text) { for (; *text && obj; ++text) obj = obj->children[*text - 'a']; return obj; }
bool trieSearch(Trie* obj, char* word) { Trie* node = trieFind(obj, word); return node && node->isWord; }
bool trieStartsWith(Trie* obj, char* prefix) { return trieFind(obj, prefix) != NULL; }
void trieFree(Trie* obj) { if (!obj) return; for (int i = 0; i < 26; ++i) trieFree(obj->children[i]); free(obj); }
