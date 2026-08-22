// LeetCode 2114 - Maximum Number of Words Found in Sentences
// https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

int mostWordsFound(char** sentences, int sentencesSize) {
    int ans = 0;
    for (int i = 0; i < sentencesSize; i++) {
        int c = 1;
        for (char* p = sentences[i]; *p; p++) if (*p == ' ') c++;
        if (c > ans) ans = c;
    }
    return ans;
}
