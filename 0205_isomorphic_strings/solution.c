// LeetCode 0205 - Isomorphic Strings
#include <stdbool.h>
#include <string.h>
bool isIsomorphic(char* s, char* t) { int mapS[256], mapT[256]; for (int i = 0; i < 256; ++i) mapS[i] = mapT[i] = -1; for (size_t i = 0; s[i] && t[i]; ++i) { unsigned char a = (unsigned char)s[i], b = (unsigned char)t[i]; if ((mapS[a] != -1 && mapS[a] != b) || (mapT[b] != -1 && mapT[b] != a)) return false; mapS[a] = b; mapT[b] = a; } return strlen(s) == strlen(t); }
