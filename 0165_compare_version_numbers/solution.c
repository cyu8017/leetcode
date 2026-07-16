// LeetCode 0165 - Compare Version Numbers
int compareVersion(char* version1, char* version2) {
    int i = 0, j = 0;
    while (version1[i] || version2[j]) {
        int a = 0, b = 0;
        while (version1[i] && version1[i] != '.') a = a * 10 + version1[i++] - '0';
        while (version2[j] && version2[j] != '.') b = b * 10 + version2[j++] - '0';
        if (a != b) return a < b ? -1 : 1;
        if (version1[i]) ++i;
        if (version2[j]) ++j;
    }
    return 0;
}