#include <list>
#include <unordered_map>
class LRUCache{int c;std::list<std::pair<int,int>>q;std::unordered_map<int,std::list<std::pair<int,int>>::iterator>m;public:LRUCache(int c):c(c){}int get(int k){if(!m.count(k))return-1;q.splice(q.begin(),q,m[k]);return m[k]->second;}void put(int k,int v){if(m.count(k)){m[k]->second=v;q.splice(q.begin(),q,m[k]);return;}if(!c)return;if(q.size()==c){m.erase(q.back().first);q.pop_back();}q.emplace_front(k,v);m[k]=q.begin();}};
