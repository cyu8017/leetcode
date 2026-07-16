#include <vector>
#include <algorithm>
using namespace std; class Solution{public:int maxProduct(vector<int>&a){int b=a[0],hi=b,lo=b;for(int i=1;i<a.size();i++){int h=hi,l=lo;hi=max(a[i],max(h*a[i],l*a[i]));lo=min(a[i],min(h*a[i],l*a[i]));b=max(b,hi);}return b;}};
