int read(char*b,int n){static char t[4];static int z,i;int k=0;while(k<n){if(i==z){z=read4(t);i=0;if(!z)break;}while(k<n&&i<z)b[k++]=t[i++];}return k;}
