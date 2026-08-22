// LeetCode 3621 - Number of Integers With Popcount Depth Equal to K I
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-i/

#include <stdlib.h>
#include <string.h>
static int popcnt(unsigned x){ int c=0; while(x){c+=x&1;x>>=1;} return c; }
static int depth_pc(int x){ if(x<=0) return 100; int d=0; while(x>1){ x=popcnt((unsigned)x); d++; } return d; }
static char sbits[70]; static int slen; static long long memo[70][2][2][70]; static char seen[70][2][2][70]; static int K;
static long long dfs(int pos, int tight, int started, int pc){
    if(pos==slen){ if(!started) return 0; if(pc==1) return K==1; return depth_pc(pc)==K-1; }
    if(seen[pos][tight][started][pc]) return memo[pos][tight][started][pc];
    int up=tight?sbits[pos]-'0':1; long long res=0;
    for(int dig=0;dig<=up;dig++){
        int nt=tight&&dig==up;
        if(!started&&dig==0) res+=dfs(pos+1,nt,0,0);
        else res+=dfs(pos+1,nt,1,pc+dig);
    }
    seen[pos][tight][started][pc]=1; return memo[pos][tight][started][pc]=res;
}
long long popcountDepth(long long n, int k) {
    if(k==0) return n>=1?1:0;
    K=k; slen=0; long long x=n; char tmp[70]; int tn=0; if(x==0){ sbits[0]='0'; slen=1; } else { while(x){ tmp[tn++]=(char)('0'+(x&1)); x>>=1; } for(int i=0;i<tn;i++) sbits[i]=tmp[tn-1-i]; slen=tn; }
    memset(seen,0,sizeof(seen));
    return dfs(0,1,0,0);
}
