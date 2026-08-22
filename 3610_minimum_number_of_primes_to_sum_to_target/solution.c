// LeetCode 3610 - Minimum Number of Primes to Sum to Target
// https://leetcode.com/problems/minimum-number-of-primes-to-sum-to-target/

#include <stdlib.h>
#include <stdbool.h>
int minNumberOfPrimes(int n, int m) {
    int primes[1000]; int pc=0, x=2;
    while(pc<m){
        bool ok=true;
        for(int i=0;i<pc && primes[i]*primes[i]<=x;i++) if(x%primes[i]==0){ok=false;break;}
        if(ok) primes[pc++]=x;
        x++;
    }
    const int inf=1000000000;
    int* f=(int*)malloc((size_t)(n+1)*sizeof(int));
    f[0]=0; for(int i=1;i<=n;i++) f[i]=inf;
    for(int i=0;i<m;i++){ int p=primes[i]; for(int j=p;j<=n;j++) if(f[j-p]+1<f[j]) f[j]=f[j-p]+1; }
    int ans=f[n]<inf?f[n]:-1; free(f); return ans;
}
