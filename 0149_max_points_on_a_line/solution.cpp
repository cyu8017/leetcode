#include <vector>
#include <map>
#include <numeric>
class Solution{public:int maxPoints(std::vector<std::vector<int>>&p){int z=0;for(int i=0;i<p.size();i++){std::map<std::pair<int,int>,int>m;for(int j=i+1;j<p.size();j++){int x=p[j][0]-p[i][0],y=p[j][1]-p[i][1],g=std::gcd(x,y);x/=g;y/=g;if(x<0||(x==0&&y<0))x=-x,y=-y;z=std::max(z,++m[{x,y}]+1);}}return p.empty()?0:z;}};
