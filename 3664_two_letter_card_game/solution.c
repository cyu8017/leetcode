// LeetCode 3664 - Two-Letter Card Game
// https://leetcode.com/problems/two-letter-card-game/

int score(char** cards, int cardsSize, char x) {
    int xx=0, left[26]={0}, right[26]={0};
    for(int i=0;i<cardsSize;i++){
        char a=cards[i][0], b=cards[i][1];
        if(a==x&&b==x) xx++; else if(a==x) left[b-'a']++; else if(b==x) right[a-'a']++;
    }
    int pairGroup(int* arr, int* rem){
        int total=0,mx=0; for(int i=0;i<26;i++){ total+=arr[i]; if(arr[i]>mx) mx=arr[i]; }
        int pairs=total/2; if(total-mx<pairs) pairs=total-mx; *rem=total-2*pairs; return pairs;
    }
    int lr,rr; int lp=pairGroup(left,&lr), rp=pairGroup(right,&rr);
    int ans=lp+rp, rem=lr+rr, use=xx<rem?xx:rem; ans+=use; xx-=use; ans+=xx/2; return ans;
}
