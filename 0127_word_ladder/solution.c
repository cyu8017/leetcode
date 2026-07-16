// LeetCode 0127 - Word Ladder
// https://leetcode.com/problems/word-ladder/

#include <string.h>
#include <stdlib.h>
static int oneAway(const char* a,const char* b){int diff=0;for(;*a;a++)if(*a!=*b&&++diff>1)return 0;return diff==1;}
int ladderLength(char* beginWord, char* endWord, char** wordList, int wordListSize) { int end=-1;for(int i=0;i<wordListSize;i++)if(!strcmp(wordList[i],endWord))end=i;if(end<0)return 0;int *dist=malloc(wordListSize*sizeof(int)),*queue=malloc((wordListSize+1)*sizeof(int)),front=0,back=1;for(int i=0;i<wordListSize;i++)dist[i]=-1;queue[0]=-1;int steps=1;while(front<back){int node=queue[front++],nextSteps=steps+1;char *word=node<0?beginWord:wordList[node];if(node==end){free(dist);free(queue);return steps;}for(int i=0;i<wordListSize;i++)if(dist[i]<0&&oneAway(word,wordList[i])){dist[i]=nextSteps;queue[back++]=i;}if(front<back&&dist[queue[front]]!=steps)steps=dist[queue[front]];}free(dist);free(queue);return 0; }