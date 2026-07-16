#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;class Solution{public:int lengthOfLongestSubstringTwoDistinct(string s){unordered_map<char,int>m;int l=0,b=0;for(int r=0;r<s.size();r++){m[s[r]]++;while(m.size()>2)if(--m[s[l]]==0)m.erase(s[l++]);else l++;b=max(b,r-l+1);}return b;}};
