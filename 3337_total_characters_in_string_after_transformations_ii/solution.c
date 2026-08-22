// LeetCode 3337 - Total Characters in String After Transformations II
// https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/

#include <stdlib.h>
#include <string.h>

static int** matNew(void) {
    int** a = (int**)malloc(26 * sizeof(int*));
    for (int i = 0; i < 26; i++) a[i] = (int*)calloc(26, sizeof(int));
    return a;
}
static void matFree(int** a) { for (int i = 0; i < 26; i++) free(a[i]); free(a); }

static int** matMul(int** a, int** b, int mod) {
    int** c = matNew();
    for (int i = 0; i < 26; i++)
        for (int k = 0; k < 26; k++) if (a[i][k])
            for (int j = 0; j < 26; j++)
                c[i][j] = (int)((c[i][j] + (long long)a[i][k] * b[k][j]) % mod);
    return c;
}

static int** matPow(int** a, int e, int mod) {
    int** r = matNew();
    for (int i = 0; i < 26; i++) r[i][i] = 1;
    int** base = matNew();
    for (int i = 0; i < 26; i++) memcpy(base[i], a[i], 26 * sizeof(int));
    while (e > 0) {
        if (e & 1) {
            int** t = matMul(r, base, mod);
            matFree(r); r = t;
        }
        int** t = matMul(base, base, mod);
        matFree(base); base = t;
        e >>= 1;
    }
    matFree(base);
    return r;
}

int lengthAfterTransformations(char* s, int t, int* nums, int numsSize) {
    (void)numsSize;
    const int mod = 1000000007;
    int** mat = matNew();
    for (int i = 0; i < 26; i++)
        for (int j = 1; j <= nums[i]; j++)
            mat[i][(i + j) % 26] = 1;
    int** mp = matPow(mat, t, mod);
    matFree(mat);
    int cnt[26] = {0};
    for (int i = 0; s[i]; i++) cnt[s[i] - 'a']++;
    int ans = 0;
    for (int i = 0; i < 26; i++)
        for (int j = 0; j < 26; j++)
            ans = (int)((ans + (long long)cnt[i] * mp[i][j]) % mod);
    matFree(mp);
    return ans;
}
