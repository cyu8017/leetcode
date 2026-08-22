// LeetCode 3728 - Stable Subarrays With Equal Boundary and Interior Sum
// https://leetcode.com/problems/stable-subarrays-with-equal-boundary-and-interior-sum/

#include <stdlib.h>
#include <string.h>

typedef struct { int first; long long second; } Key;
#define HS 200003
static Key kk[HS];
static int kv[HS];
static char ku[HS];
static void kc(void){memset(ku,0,sizeof(ku));}
static unsigned kh(Key k){ return ((unsigned)k.first*1000003u+(unsigned)(k.second%1000003))%HS; }
static int* kg(Key k){
    unsigned i=kh(k);
    for(;;){ if(!ku[i]){ku[i]=1;kk[i]=k;kv[i]=0;return &kv[i];}
      if(kk[i].first==k.first&&kk[i].second==k.second)return &kv[i];
      if(++i==HS)i=0; }
}
static int khas(Key k){
    unsigned i=kh(k);
    for(;;){ if(!ku[i])return 0;
      if(kk[i].first==k.first&&kk[i].second==k.second)return kv[i];
      if(++i==HS)i=0; }
}

long long countStableSubarrays(int* capacity, int capacitySize) {
    int n = capacitySize;
    long long* s = (long long*)calloc((size_t)(n + 1), sizeof(long long));
    for (int i = 1; i <= n; i++) s[i] = s[i - 1] + capacity[i - 1];
    kc();
    long long ans = 0;
    for (int r = 2; r < n; r++) {
        int l = r - 2;
        Key keyL = {capacity[l], (long long)capacity[l] + s[l + 1]};
        (*kg(keyL))++;
        Key keyR = {capacity[r], s[r]};
        ans += khas(keyR);
    }
    free(s);
    return ans;
}
