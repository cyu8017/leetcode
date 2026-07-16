class Solution{public:int read(char*b,int n){char t[4];int k=0;while(k<n){int c=read4(t);if(!c)break;for(int i=0;i<c&&k<n;i++)b[k++]=t[i];}return k;}};
