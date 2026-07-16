// LeetCode 0126 - Word Ladder II
// https://leetcode.com/problems/word-ladder-ii/

func findLadders(beginWord string, endWord string, wordList []string) [][]string {
    words := map[string]bool{}; for _, w := range wordList { words[w] = true }; if !words[endWord] { return [][]string{} }
    parents := map[string][]string{}; queue := []string{beginWord}; seen := map[string]bool{beginWord:true}; found := false
    for len(queue)>0 && !found { level := map[string]bool{}; size:=len(queue); for ; size>0; size-- { word:=queue[0]; queue=queue[1:]; bytes:=[]byte(word); for i:=range bytes { saved:=bytes[i]; for c:=byte('a'); c<='z'; c++ { bytes[i]=c; next:=string(bytes); if words[next] && !seen[next] { if !level[next] { level[next]=true; queue=append(queue,next) }; parents[next]=append(parents[next],word) } }; bytes[i]=saved } }; for w:=range level { seen[w]=true }; found=level[endWord] }
    if !found { return [][]string{} }; result:=[][]string{}; path:=[]string{endWord}; var dfs func(string); dfs=func(word string) { if word==beginWord { row:=make([]string,len(path)); for i:=range path { row[len(path)-1-i]=path[i] }; result=append(result,row); return }; for _, p:=range parents[word] { path=append(path,p); dfs(p); path=path[:len(path)-1] } }; dfs(endWord); return result
}