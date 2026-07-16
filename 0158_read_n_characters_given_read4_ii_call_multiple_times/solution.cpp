class Solution{char t[4];int z=0,i=0;public:int read(char*b,int n){int k=0;while(k<n){if(i==z){z=read4(t);i=0;if(!z)break;}while(k<n&&i<z)b[k++]=t[i++];}return k;}};
