#include <stdlib.h>
#include <string.h>
char* reverseWords(char*s){int n=strlen(s),k=0;char*r=malloc(n+1);for(char*e=s+n;e>s;){while(e>s&&e[-1]==' ')e--;char*b=e;while(b>s&&b[-1]!=' ')b--;if(b==e)break;if(k)r[k++]=' ';memcpy(r+k,b,e-b);k+=e-b;e=b;}r[k]=0;return r;}
