// LeetCode 3625 - Count Number of Trapezoids II
// https://leetcode.com/problems/count-number-of-trapezoids-ii/

#include <stdlib.h>
/* Port using rational slope keys as (dy,dx) reduced + intercept as long double-ish via int64 */
static long long gcdll(long long a,long long b){ if(a<0)a=-a; if(b<0)b=-b; while(b){ long long t=a%b;a=b;b=t;} return a; }
typedef struct { long long k1,k2,b1,b2; int cnt; } Ent1;
typedef struct { int p; long long k1,k2; int cnt; } Ent2;
int countTrapezoids(int** points, int pointsSize, int* pointsColSize) {
    (void)pointsColSize;
    int n=pointsSize, cap=n*n+8;
    Ent1* c1=(Ent1*)calloc((size_t)cap,sizeof(Ent1)); int n1=0;
    Ent2* c2=(Ent2*)calloc((size_t)cap,sizeof(Ent2)); int n2=0;
    for(int i=0;i<n;i++) for(int j=0;j<i;j++){
        long long x1=points[i][0],y1=points[i][1],x2=points[j][0],y2=points[j][1];
        long long dx=x2-x1, dy=y2-y1, k1,k2,b1,b2;
        if(dx==0){ k1=1; k2=0; b1=x1; b2=1; } /* vertical sentinel k=1/0 */
        else { long long g=gcdll(dy,dx); k1=dy/g; k2=dx/g; if(k2<0){k1=-k1;k2=-k2;}
            /* b = (y1*dx - x1*dy)/dx  store as num/den */
            b1=y1*dx-x1*dy; b2=dx; long long g2=gcdll(b1,b2); b1/=g2; b2/=g2; if(b2<0){b1=-b1;b2=-b2;}
        }
        int f=-1; for(int t=0;t<n1;t++) if(c1[t].k1==k1&&c1[t].k2==k2&&c1[t].b1==b1&&c1[t].b2==b2){f=t;break;}
        if(f<0) c1[n1++]=(Ent1){k1,k2,b1,b2,1}; else c1[f].cnt++;
        int p=(int)((x1+x2+2000)*4000+(y1+y2+2000));
        f=-1; for(int t=0;t<n2;t++) if(c2[t].p==p&&c2[t].k1==k1&&c2[t].k2==k2){f=t;break;}
        if(f<0) c2[n2++]=(Ent2){p,k1,k2,1}; else c2[f].cnt++;
    }
    /* group c1 by slope */
    int ans=0;
    for(int i=0;i<n1;i++){
        int s=0;
        for(int j=0;j<n1;j++) if(c1[j].k1==c1[i].k1&&c1[j].k2==c1[i].k2){
            /* process each slope once: when i is first of that slope */
        }
    }
    /* better: for each unique slope accumulate */
    for(int i=0;i<n1;i++){
        int first=1; for(int j=0;j<i;j++) if(c1[j].k1==c1[i].k1&&c1[j].k2==c1[i].k2){first=0;break;}
        if(!first) continue;
        int s=0;
        for(int j=0;j<n1;j++) if(c1[j].k1==c1[i].k1&&c1[j].k2==c1[i].k2){ ans+=s*c1[j].cnt; s+=c1[j].cnt; }
    }
    for(int i=0;i<n2;i++){
        int first=1; for(int j=0;j<i;j++) if(c2[j].p==c2[i].p){first=0;break;}
        if(!first) continue;
        int s=0;
        for(int j=0;j<n2;j++) if(c2[j].p==c2[i].p){ ans-=s*c2[j].cnt; s+=c2[j].cnt; }
    }
    free(c1); free(c2); return ans;
}
