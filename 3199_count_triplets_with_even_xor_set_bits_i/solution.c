// LeetCode 3199 - Count Triplets with Even XOR Set Bits I
// https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-i/

static int pc3199(unsigned x) { int c = 0; while (x) { c += x & 1; x >>= 1; } return c; }

int tripletCount(int* a, int aSize, int* b, int bSize, int* c, int cSize) {
    int cnt1[2] = {0}, cnt2[2] = {0}, cnt3[2] = {0};
    for (int i = 0; i < aSize; i++) cnt1[pc3199((unsigned)a[i]) % 2]++;
    for (int i = 0; i < bSize; i++) cnt2[pc3199((unsigned)b[i]) % 2]++;
    for (int i = 0; i < cSize; i++) cnt3[pc3199((unsigned)c[i]) % 2]++;
    int ans = 0;
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++)
            for (int k = 0; k < 2; k++)
                if ((i + j + k) % 2 == 0) ans += cnt1[i] * cnt2[j] * cnt3[k];
    return ans;
}
