// LeetCode 0127 - Word Ladder
// https://leetcode.com/problems/word-ladder/

func ladderLength(beginWord string, endWord string, wordList []string) int {
    words:=map[string]bool{}; for _,w:=range wordList { words[w]=true }; if !words[endWord] { return 0 }
    queue:=[]string{beginWord}; seen:=map[string]bool{beginWord:true}; steps:=1
    for len(queue)>0 { size:=len(queue); for ;size>0;size-- { word:=queue[0];queue=queue[1:]; if word==endWord{return steps}; chars:=[]byte(word); for i:=range chars { saved:=chars[i];for c:=byte('a');c<='z';c++ {chars[i]=c;next:=string(chars);if words[next]&&!seen[next]{seen[next]=true;queue=append(queue,next)}};chars[i]=saved } };steps++ };return 0
}