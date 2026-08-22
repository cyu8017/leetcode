// LeetCode 3589 - Count Prime-Gap Balanced Subarrays
// https://leetcode.com/problems/count-prime-gap-balanced-subarrays/

#include <stdlib.h>
#include <stdbool.h>
int primeSubarray(int* nums, int numsSize, int k) {
    int mx=0; for(int i=0;i<numsSize;i++) if(nums[i]>mx) mx=nums[i];
    bool* isPrime=(bool*)calloc((size_t)mx+1,sizeof(bool));
    for(int i=2;i<=mx;i++) isPrime[i]=true;
    for(int i=2;i*i<=mx;i++) if(isPrime[i]) for(int j=i*i;j<=mx;j+=i) isPrime[j]=false;
    int ans=0, n=numsSize;
    for(int l=0;l<n;l++){
        int primes[200]; int pc=0; /* enough for typical constraints; grow if needed */
        int* pr=primes; int pcap=200; int* heap=NULL;
        for(int r=l;r<n;r++){
            if(isPrime[nums[r]]){
                if(pc==pcap){ pcap*=2; if(!heap){heap=malloc((size_t)pcap*sizeof(int)); for(int t=0;t<pc;t++)heap[t]=pr[t]; pr=heap;} else pr=realloc(pr,(size_t)pcap*sizeof(int)); }
                pr[pc++]=nums[r];
            }
            if(pc>=2){
                int mn=pr[0], mxp=pr[0];
                for(int t=1;t<pc;t++){ if(pr[t]<mn)mn=pr[t]; if(pr[t]>mxp)mxp=pr[t]; }
                if(mxp-mn<=k) ans++;
            }
        }
        free(heap);
    }
    free(isPrime); return ans;
}
