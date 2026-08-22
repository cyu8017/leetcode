// LeetCode 3616 - Number of Student Replacements
// https://leetcode.com/problems/number-of-student-replacements/

int totalReplacements(int* ranks, int ranksSize) {
    int ans=0,cur=ranks[0];
    for(int i=0;i<ranksSize;i++) if(ranks[i]<cur){cur=ranks[i];ans++;}
    return ans;
}
