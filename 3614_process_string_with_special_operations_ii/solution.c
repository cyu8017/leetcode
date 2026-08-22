// LeetCode 3614 - Process String with Special Operations II
// https://leetcode.com/problems/process-string-with-special-operations-ii/

#include <string.h>
char processStr(char* s, long long k) {
    long long m=0; int n=(int)strlen(s);
    for(int i=0;i<n;i++){
        char c=s[i];
        if(c=='*') m=m-1>0?m-1:0;
        else if(c=='#') m<<=1;
        else if(c!='%') m+=1;
    }
    if(k>=m) return '.';
    for(int i=n-1;;i--){
        char c=s[i];
        if(c=='*') m+=1;
        else if(c=='#'){ m/=2; if(k>=m) k-=m; }
        else if(c=='%') k=m-1-k;
        else { m-=1; if(k==m) return c; }
    }
}
