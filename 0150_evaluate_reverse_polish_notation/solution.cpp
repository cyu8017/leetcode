#include <vector>
#include <string>
class Solution{public:int evalRPN(std::vector<std::string>&t){std::vector<int>s;for(auto&x:t)if(x.size()==1&&std::string("+-*/").find(x)!=std::string::npos){int b=s.back();s.pop_back();int a=s.back();s.pop_back();s.push_back(x=="+"?a+b:x=="-"?a-b:x=="*"?a*b:a/b);}else s.push_back(stoi(x));return s.back();}};
