// LeetCode 0771 - Jewels and Stones
// https://leetcode.com/problems/jewels-and-stones/

int numJewelsInStones(char* jewels, char* stones) {
    int jewel[256] = {0};
    for (char* p = jewels; *p; p++) jewel[(unsigned char)*p] = 1;
    int ans = 0;
    for (char* p = stones; *p; p++) if (jewel[(unsigned char)*p]) ans++;
    return ans;
}
