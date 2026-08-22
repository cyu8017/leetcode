// LeetCode 2645 - Minimum Additions to Make Valid String
// https://leetcode.com/problems/minimum-additions-to-make-valid-string/

int addMinimum(char* word) {
    int ans = 0, expect = 0, i = 0;
    while (word[i]) {
        char need = (char)('a' + expect);
        if (word[i] == need) i++;
        else ans++;
        expect = (expect + 1) % 3;
    }
    ans += (3 - expect) % 3;
    return ans;
}
