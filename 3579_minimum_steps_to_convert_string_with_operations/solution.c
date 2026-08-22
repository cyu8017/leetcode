// LeetCode 3579 - Minimum Steps to Convert String with Operations
// https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/

#include <stdlib.h>
#include <string.h>
#include <limits.h>
static int imin(int a,int b){return a<b?a:b;}
int minOperations(char* word1, char* word2) {
    int n=(int)strlen(word1);
    int* f=(int*)malloc((size_t)(n+1)*sizeof(int));
    for(int i=0;i<=n;i++) f[i]=INT_MAX/4; f[0]=0;
    for(int i=1;i<=n;i++){
        for(int j=0;j<i;j++){
            int cnt[26][26]={0}; int res=0;
            for(int p=j;p<i;p++){
                int a=word1[p]-'a', b=word2[p]-'a';
                if(a!=b){ if(cnt[b][a]>0) cnt[b][a]--; else { cnt[a][b]++; res++; } }
            }
            int a=res;
            memset(cnt,0,sizeof(cnt)); res=0;
            for(int p=j;p<i;p++){
                int jj=i-1-(p-j);
                int aa=word1[jj]-'a', bb=word2[p]-'a';
                if(aa!=bb){ if(cnt[bb][aa]>0) cnt[bb][aa]--; else { cnt[aa][bb]++; res++; } }
            }
            int b=1+res;
            f[i]=imin(f[i], f[j]+imin(a,b));
        }
    }
    int ans=f[n]; free(f); return ans;
}
