// LeetCode 3714 - Longest Balanced Substring II
// https://leetcode.com/problems/longest-balanced-substring-ii/

#include <string.h>
#include <stdlib.h>

static int imax(int a, int b) { return a > b ? a : b; }

static int calc1(char* s) {
    int res = 0, n = (int)strlen(s), i = 0;
    while (i < n) {
        int j = i + 1;
        while (j < n && s[j] == s[i]) j++;
        if (j - i > res) res = j - i;
        i = j;
    }
    return res;
}

#define HS 200003
static int hk[HS], hv[HS];
static char hu[HS];
static void hclear(void) { memset(hu, 0, sizeof(hu)); }
static int* hget(int k, int* created) {
    unsigned i = (unsigned)k % HS;
    for (;;) {
        if (!hu[i]) { hu[i]=1; hk[i]=k; hv[i]=0; if(created)*created=1; return &hv[i]; }
        if (hk[i]==k) { if(created)*created=0; return &hv[i]; }
        if (++i==HS) i=0;
    }
}
static int hhas(int k, int* out) {
    unsigned i = (unsigned)k % HS;
    for (;;) {
        if (!hu[i]) return 0;
        if (hk[i]==k) { *out = hv[i]; return 1; }
        if (++i==HS) i=0;
    }
}
static void hput(int k, int v) {
    int c; int* p = hget(k, &c); *p = v;
}

static int calc2(char* s, char a, char b) {
    int res = 0, n = (int)strlen(s), i = 0;
    while (i < n) {
        while (i < n && s[i] != a && s[i] != b) i++;
        hclear();
        hput(0, i - 1);
        int d = 0;
        while (i < n && (s[i] == a || s[i] == b)) {
            if (s[i] == a) d++; else d--;
            int prev;
            if (hhas(d, &prev)) {
                if (i - prev > res) res = i - prev;
            } else hput(d, i);
            i++;
        }
    }
    return res;
}

typedef struct { int x, y; } Key;
#define HS2 400009
static Key k2[HS2];
static int v2[HS2];
static char u2[HS2];
static void c2(void){memset(u2,0,sizeof(u2));}
static unsigned hash2(Key k){ return ((unsigned)k.x*10007u+(unsigned)k.y)%HS2; }
static int has2(Key k, int* out){
    unsigned i=hash2(k);
    for(;;){ if(!u2[i])return 0; if(k2[i].x==k.x&&k2[i].y==k.y){*out=v2[i];return 1;} if(++i==HS2)i=0; }
}
static void put2(Key k, int v){
    unsigned i=hash2(k);
    for(;;){ if(!u2[i]){u2[i]=1;k2[i]=k;v2[i]=v;return;} if(k2[i].x==k.x&&k2[i].y==k.y){v2[i]=v;return;} if(++i==HS2)i=0; }
}

static int calc3(char* s) {
    c2();
    put2((Key){0,0}, -1);
    int cnt[3] = {0};
    int res = 0;
    int n = (int)strlen(s);
    for (int i = 0; i < n; i++) {
        cnt[s[i] - 'a']++;
        Key k = {cnt[0] - cnt[1], cnt[1] - cnt[2]};
        int j;
        if (has2(k, &j)) {
            if (i - j > res) res = i - j;
        } else put2(k, i);
    }
    return res;
}

int longestBalanced(char* s) {
    int x = calc1(s);
    int y = imax(calc2(s, 'a', 'b'), imax(calc2(s, 'b', 'c'), calc2(s, 'a', 'c')));
    int z = calc3(s);
    return imax(x, imax(y, z));
}
