#include <sstream>
#include <string>
using namespace std; class Solution{public:string reverseWords(string s){istringstream x(s);string w,r;while(x>>w)r=r.empty()?w:w+" "+r;return r;}};
