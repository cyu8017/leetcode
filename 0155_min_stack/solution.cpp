#include <vector>
#include <algorithm>
using namespace std;class MinStack{vector<int>a,m;public:void push(int x){a.push_back(x);m.push_back(m.empty()?x:min(x,m.back()));}void pop(){a.pop_back();m.pop_back();}int top(){return a.back();}int getMin(){return m.back();}};
